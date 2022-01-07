import dash
from dash.dependencies import Input, Output, State, ALL
from dash.exceptions import PreventUpdate

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np

from dash_app import app
import dash_layout as dl


input_1 = \
    {'label': 'Input1', 'type': 'input', 'dimensions': '-', 'size_label': 'xl',
     'sim_name': ['input', '1'], 'value': np.round(np.random.rand(), 2)}
input_2 = \
    {'label': 'Input2', 'type': 'input', 'dimensions': '', 'size_label': 'xl',
     'sim_name': ['input', '2'],
     'value': np.round(np.random.rand(), 2)}
input_3 = \
    {'label': 'Input3', 'type': 'input', 'dimensions': 'm', 'size_label': 'xl',
     'sim_name': ['input', '3'],
     'value': np.round(np.random.rand(), 2)}
input_4 = \
    {'label': 'Input4', 'type': 'input', 'dimensions': 'm²', 'size_label': 'xl',
     'sim_name': ['input', '4'],
     'value': np.round(np.random.rand(), 2)}
sub_frame1 = \
    {'title': 'Type: Input, Specifier: False', 'show_title': True,
     'className': 'title divider', 'size_label': 'xl',
     'widget_dicts': [input_1, input_2, input_3, input_4]}
input2 = \
    {'label': 'Input5', 'type': 'input', 'types': 'multiinput',
     'size_label': 'l', 'dimensions': 'km', 'value': np.round(np.random.rand(), 2),
     'sim_name': ['input', '5'], 'number': 2}

sub_frame2 = \
    {'title': 'Type: Input, Specifier: 1 Output Component with 2 Inputs',
     'show_title': True, 'className': 'title divider', 'size_label': 'l',
     'widget_dicts': [input2]}
label2_inp3 = \
    {'type': 'label', 'size_label': 's', 'label': 'Input A', 'row': 1,
     'column': 1}
label3_inp3 = \
    {'type': 'label', 'size_label': 's', 'label': 'Input B',
     'row': 1, 'column': 2}
label4_inp3 = \
    {'type': 'label', 'size_label': 's', 'label': 'Input new',
     'row': 2, 'column': 1}
label5_inp3 = \
    {'type': 'label', 'size_label': 's', 'label': 'Input old', 'row':2,
     'column': 2}
label6_inp3 = \
    {'type': 'label', 'size_label': 's', 'label': 'Input he', 'row': 2,
     'column': 3}
label7_inp3 = \
    {'type': 'label', 'size_label': 's', 'label': 'Input ha', 'row': 2,
     'column': 4}
label_inp3 = \
    {'type': 'label', 'size_label': 's', 'label': 'Inputbereich',
     'sticky': 'WNS', 'font': 'bold'}

input3 = \
    {'label': 'Input6', 'type': 'input', 'size_label': 's', 'dimensions': 'm',
     'types': 'multiinput', 'value': [[1, 2], [3, 4]], 'number': 4,
     'sim_name': [['input', '6', 'a', [0, 1]],
                  ['input', '6', 'b', [2, 3]]]}
# ['input6a', 'input6b']
sub_frame3 = \
    {'title': 'Type: Input, Specifier: 2 Output Components with 4 Inputs',
     'show_title': True, 'className': 'title divider', 'size_label': 's',
     'widget_dicts': [label2_inp3, label3_inp3, input3]}

tab_dict = {'title': 'Tab1',
            'sub_frame_dicts': [sub_frame1, sub_frame2, sub_frame3]}

tab_layout = \
    html.Div(dl.frame(tab_dict), className='neat-spacing')