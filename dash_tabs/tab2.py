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
