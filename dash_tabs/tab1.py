import dash
from dash.dependencies import Input, Output, State, ALL
from dash.exceptions import PreventUpdate

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np

from dash_app import app
import dash_layout as dl


tab_layout = \
    html.Div(
        [html.Div('Type: Input, Specifier: False', className='title divider'),
         dl.row_input(f'Input_1', value=np.round(np.random.rand(), 2),
                      unit='-', size_label='xl', ids='input_1'),
         # {type: input, id: input_1, specifier: False}
         dl.row_input(f'Input_2', value=np.round(np.random.rand(), 2),
                      size_label='xl', ids='input_2'),
         # {type: input, id: input_2, specifier: False}
         dl.row_input(f'Input_3', value=np.round(np.random.rand(), 2),
                      unit='m', size_label='xl', ids='input_3'),
         # {type: input, id: input_3, specifier: False}
         dl.row_input(f'Input_4', value=np.round(np.random.rand(), 2),
                      unit='m²', size_label='xl', ids='input_4'),
         # {type: input, id: input_4, specifier: False}

         html.Div('Type: Input, Specifier: 1 Output Component with 2 Inputs',
                  className='title divider'),
         html.Div(  # total 4 ids components, output should be 2 ids components
             dl.row_input(f'Input2', types='multiinput', size_label='l',
                          unit='km', value=np.round(np.random.rand(), 2),
                          ids=['input2_1a', 'input2_1b'])),
         # {type: multiinput, id: input2_1a, specifier: False},
         # {type: multiinput, id: input2_2a, specifier: False}

         html.Div('Type: Input, Specifier: 2 Output Components with 4 Inputs',
                  className='title divider'),
         html.Div(  # total 8 ids components, output should be 4 ids components
             dl.row_input(f'Input3', types='multiinput', size_label='m',
                          unit='s', value=np.round(np.random.rand(), 2),
                          ids=['input3_1a', 'input3_2a',
                               'input3_1b', 'input3_2b']))],
        # {type: multiinput, id: input3_1a, specifier: False},
        # {type: multiinput, id: input3_1b, specifier: False},
        # {type: multiinput, id: input3_2a, specifier: False},
        # {type: multiinput, id: input3_2b, specifier: False},

        className='neat-spacing')


# @app.callback(
#