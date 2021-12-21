import dash
from dash.dependencies import Input, Output, State, ALL
from dash.exceptions import PreventUpdate

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np

from dash_app import app

tab_layout = \
    html.Div(
        [html.Div('Type: Tab2, Specifier: Activate/Visibility',
                  className='title divider'),
         dbc.Checklist(
            options=[{"label": "Activate Dropdown", "value": 1}],
            value=[1],
            id={'type': 'input', 'id': 'checklist', 'specifier': 'activate'},
            inline=True, persistence=True,
            persistence_type="memory",
            style={'justify-content': 'center',
                   'margin-left': '20%', 'display': 'flex'}),
            html.Div(dcc.Dropdown(
                id={'type': 'input', 'id': 'dropdown1',
                    'specifier': 'visibility'},
                options=[{'label': 'Kuala Lumpur', 'value': 'KL'},
                         {'label': 'Singapore', 'value': 'SG'},
                         {'label': 'Bangkok', 'value': 'BKK'}], value='KL'),
                id={'type': 'container', 'id': 'dropdown1', 'specifier':
                    'visibility'}),
            html.Div(dcc.Dropdown(
                id={'type': 'input', 'id': 'dropdown2',
                    'specifier': 'disabled'},
                options=[{'label': 'New York City', 'value': 'NYC'},
                         {'label': 'Montreal', 'value': 'MTL'},
                         {'label': 'San Francisco', 'value': 'SF'}],
                value='NYC'))], className='neat-spacing')


@app.callback(
    [Output({'type': 'container', 'id': ALL, 'specifier': 'visibility'},
            'style'),
     Output({'type': 'input', 'id': ALL, 'specifier': 'disabled'},
            'disabled')],
    Input({'type': 'input', 'id': 'checklist', 'specifier': 'activate'},
          'value'),
    # also works Input({type:ALL, id:ALL, specifier: 'activate'}, 'value);
    # needed at least one similar key-value pair
)
def visibility_dropdown(checklist):
    """
    When using ALL for output, it is worth noting that it needs to return
    list since ALL will include all the value/ids that fits with the keys of
    the id inside the list of .
    """
    if checklist.__contains__(1):
        disabled = [False]
        style = [None]
    else:
        disabled = [True]
        style = [{'display': 'none'}]

    return style, disabled

#
# y =Div(children=
#        [Div(children='Type: Input, Specifier: False', className='title divider'),
#         Div(children=[Label(children='Input_1', className='label-param-xl g-0'),
#                       Div(children=[Input(id={'type': 'input', 'id': 'input_1', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.17)], className='centered r_flex g-0', style={'width': '25%'}),
#                       Div(children='-', className='ufontm centered g-0')], className='row-lay r_flex g-0'),
#         Div(children=[Label(children='Input_2', className='label-param-xl g-0'),
#                       Div(children=[Input(id={'type': 'input', 'id': 'input_2', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.04)], className='centered r_flex g-0', style={'width': '25%'}),
#                       Div(children='', className='ufontm centered g-0')], className='row-lay r_flex g-0'),
#         Div(children=[Label(children='Input_3', className='label-param-xl g-0'),
#                       Div(children=[Input(id={'type': 'input', 'id': 'input_3', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.04)], className='centered r_flex g-0', style={'width': '25%'}),
#                       Div(children='m', className='ufontm centered g-0')], className='row-lay r_flex g-0'),
#         Div(children=[Label(children='Input_4', className='label-param-xl g-0'),
#                       Div(children=[Input(id={'type': 'input', 'id': 'input_4', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.02)], className='centered r_flex g-0', style={'width': '25%'}),
#                       Div(children='m²', className='ufontm centered g-0')], className='row-lay r_flex g-0'),
#         Div(children='Type: Input, Specifier: 1 Output Component with 2 Inputs', className='title divider'),
#         Div(Div(children=[Label(children='Input2', className='label-param-l g-0'),
#                           Div(children=[Input(id={'type': 'multiinput', 'id': 'input2_1a', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.48),
#                                         Input(id={'type': 'multiinput', 'id': 'input2_1b', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.48)], className='centered r_flex g-0', style={'width': '45%'}),
#                           Div(children='km', className='ufontm centered g-0')], className='row-lay r_flex g-0')),
#         Div(children='Type: Input, Specifier: 2 Output Components with 4 Inputs', className='title divider'),
#         Div(Div(children=[Label(children='Input3', className='label-param-m g-0'),
#                           Div(children=[Input(id={'type': 'multiinput', 'id': 'input3_1a', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.17),
#                                         Input(id={'type': 'multiinput', 'id': 'input3_2a', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.17),
#                                         Input(id={'type': 'multiinput', 'id': 'input3_1b', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.17),
#                                         Input(id={'type': 'multiinput', 'id': 'input3_2b', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.17)],
#                               className='centered r_flex g-0', style={'width': '50%'}),
#                           Div(children='s', className='ufontm centered g-0')], className='row-lay r_flex g-0'))], className='neat-spacing')
#
# x = Div(children=
#         Div([Div([Div(children=[Label(children='Input_1', className='label-param-xl g-0'),
#                                 Div(children=
#                                     [Input(id={'type': 'input', 'id': 'input_1', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.29)], className='centered r_flex g-0', style={'width': '25%'}),
#                                 Div(children='-', className='ufontm centered g-0')], className='row-lay r_flex g-0'),
#                   Div(children=[Label(children='Input_2', className='label-param-xl g-0'),
#                                 Div(children=
#                                     [Input(id={'type': 'input', 'id': 'input_2', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=1.0)], className='centered r_flex g-0', style={'width': '25%'}),
#                                 Div(children='', className='ufontm centered g-0')], className='row-lay r_flex g-0'),
#                   Div(children=[Label(children='Input_3', className='label-param-xl g-0'),
#                                 Div(children=
#                                     [Input(id={'type': 'input', 'id': 'input_3', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.85)], className='centered r_flex g-0', style={'width': '25%'}),
#                                 Div(children='m', className='ufontm centered g-0')], className='row-lay r_flex g-0'),
#                   Div(children=[Label(children='Input_4', className='label-param-xl g-0'),
#                                 Div(children=
#                                     [Input(id={'type': 'input', 'id': 'input_4', 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.45)], className='centered r_flex g-0', style={'width': '25%'}),
#                                 Div(children='m²', className='ufontm centered g-0')], className='row-lay r_flex g-0')]),
#              Div([Div(children=[Label(children='Input2', className='label-param-l g-0'),
#                                 Div(children=
#                                     [Input(id={'type': 'multiinput', 'id': 0, 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.48),
#                                      Input(id={'type': 'multiinput', 'id': 1, 'specifier': False}, className='val_input', debounce=True, disabled=False, persistence=True, persistence_type='memory', value=0.48)], className='centered r_flex g-0', style={'width': '45%'}),
#                                 Div(children='km', className='ufontm centered g-0')], className='row-lay r_flex g-0')]),
#              Div([Div(children=[Label(children='Input3', className='label-param g-0'),
#                                 Div(children=[], className='centered r_flex g-0', style={'width': '57%'}),
#                                 Div(children='m', className='ufontm centered g-0')], className='row-lay r_flex g-0')])]), className='neat-spacing')

