
import dash
from dash.dependencies import Input, Output, State, ALL  #
from dash.exceptions import PreventUpdate
from dash import dcc
from dash import html
from dash_tabs import tab1, tab2
from dash import dash_table as dt
import collections

import base64
import io
import json

import dash_layout as dl
import dash_function as df
# import dash_modal as dm


from dash_app import app


tabs_list = [tab1.tab_layout, tab2.tab_layout]

app.layout = \
    html.Div(
        [html.Div(
            [html.Div(
                dl.tab_container(
                    tabs_list,
                    label=[f'Tab_{n+1}' for n, k in enumerate(tabs_list)],
                    ids=[f'tab{n+1}' for n, v in enumerate(tabs_list)])),
             html.Div(
                 [html.Div(
                     [html.Button('Simulate', id='sim-button'),
                      html.Button('Save', id='save-button')]),
                  dcc.Download(id="savefile-json"),
                  dcc.Upload(id="upload-file",
                             children=html.Div(['Drag and Drop or ',
                                                html.A('Select Files',
                                                       style=
                                                       {'font-weight': 'bold',
                                                        'text-decoration':
                                                            'underline'})]),
                             style={'width': '100%', 'height': '60px',
                                    'lineHeight': '60px', 'borderWidth': '1px',
                                    'borderStyle': 'dashed',  'margin': 'auto',
                                    'borderRadius': '5px',
                                    'textAlign': 'center'},
                             accept='.json', className='dragndrop')])],
            id='left-column', className='four columns'),
         html.Div(
             [dt.DataTable(id='table', editable=True,
                           column_selectable='multi')],
             style={'border': '1px solid lightgrey', 'overflow': 'auto'},
             className='eight columns')], className='flex-display')


@app.callback(
    Output('table', 'columns'),
    Output('table', 'data'),
    Output('sim-button', 'n_clicks'),
    Input('sim-button', 'n_clicks'),
    State({'type': 'input', 'id': ALL, 'specifier': ALL}, 'value'),
    State({'type': 'multiinput', 'id': ALL, 'specifier': False}, 'value'),
    State({'type': 'input', 'id': ALL, 'specifier': ALL}, 'id'),
    State({'type': 'multiinput', 'id': ALL, 'specifier': False}, 'id'),
)
def run_simulation(n_click, inputs, inputs2, ids, ids2):
    ctx = dash.callback_context.triggered[0]['prop_id']
    if n_click is None:
        raise PreventUpdate
    else:
        # id2 = {id_l['id'][:-2]: num for num, id_l in enumerate(ids2)}  # :-1
        # # remove multiple ids for multiinputs
        # id_list = [id_l['id'] for id_l in ids]+list(id2.keys())
        #
        # inputs2 = df.multi_inputs(inputs2)
        # print(inputs2)
        # new_inputs = []
        # for val in inputs+inputs2:
        #     new_val = list(df.unstringify(val))[0]
        #
        #     if isinstance(new_val, list):
        #         if len(new_val) == 0:
        #             new_val = bool(new_val)
        #         else:
        #             if len(new_val) == 1 and new_val[0] == 1:
        #                 new_val = bool(new_val)
        #     new_inputs.append(new_val)
        #
        # new_ids = [id_l['id'] for id_l in ids] + [id_l['id'] for id_l in ids2]
        # dict_data = {}
        # for id_l, v_l in zip(new_ids, new_inputs):
        #     dict_data.update({id_l: v_l})
        # new_dict_data = df.multi_inputs(dict_data)
        new_dict_data = df.process_inputs(inputs, inputs2, ids, ids2)
        # print(new_dict_data)

        index = [{'id': 'IDs', 'name': 'IDs'}, {'id': 'Value', 'name': 'Value'}]
        datas = [{'IDs': id_l, 'Value': val} if not isinstance(val, list)
                 else {'IDs': id_l, 'Value': f'{[v for v in val]}'}
                 for id_l, val in
                 zip(new_dict_data.keys(), new_dict_data.values())]

        return index, datas, None


@app.callback(
    Output({'type': 'input', 'id': ALL, 'specifier': ALL}, 'value'),
    Output({'type': 'multiinput', 'id': ALL, 'specifier': False}, 'value'),
    Output('upload-file', 'contents'),
    Input('upload-file', 'contents'),
    State({'type': 'input', 'id': ALL, 'specifier': ALL}, 'id'),
    State({'type': 'multiinput', 'id': ALL, 'specifier': False}, 'id'),
    State({'type': 'input', 'id': ALL, 'specifier': ALL}, 'value'),
    State({'type': 'multiinput', 'id': ALL, 'specifier': False}, 'value')
)
def upload_simulation(contents, ids, ids2, state1, state2):
    if contents is None:
        raise PreventUpdate
    else:
        try:

            j_file = df.parse_contents(contents)

            list_ids = [id_l['id'] for id_l in ids]
            list_ids2 = [id_l['id'] for id_l in ids2]

            dict_ids = {id_l: num for num, id_l in enumerate(list_ids)}
            dict_ids2 = {id_l: num for num, id_l in enumerate(list_ids2)}

            for k, v in j_file.items():
                if isinstance(v, list):
                    for num, val in enumerate(v):
                        dict_ids2[k+f'_{num}'] = val
                else:
                    if isinstance(v, bool):
                        if v is True:
                            dict_ids[k] = [1]
                        else:
                            dict_ids[k] = []
                    else:
                        dict_ids[k] = v

            return list(dict_ids.values()), list(dict_ids2.values()), None
        except Exception:
            print('error')
            return state1, state2, None


@app.callback(
    Output("savefile-json", "data"),
    Output('save-button', "n_clicks"),
    Input('save-button', "n_clicks"),
    State({'type': 'input', 'id': ALL, 'specifier': ALL}, 'id'),
    State({'type': 'multiinput', 'id': ALL, 'specifier': False}, 'id'),
    State({'type': 'input', 'id': ALL, 'specifier': ALL}, 'value'),
    State({'type': 'multiinput', 'id': ALL, 'specifier': False}, 'value'),
    prevent_initial_call=True,
)
def save_simulation(n_clicks, ids, ids2, val1, val2):
    if n_clicks is not None:
        dict_data = df.process_inputs(val1, val2, ids, ids2)  # values first
        sep_id_list = [joined_id.split('-') for joined_id in
                       dict_data.keys()]
        val_list = dict_data.values()
        new_dict = {}
        for path, vals in zip(sep_id_list, val_list):
            current_level = new_dict
            for part in path:
                if part not in current_level:
                    if part != path[-1]:
                        current_level[part] = {}
                    else:
                        current_level[part] = vals
                current_level = current_level[part]

        return dict(content=json.dumps(new_dict, indent=2),
                    filename="test.json"), None


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)
