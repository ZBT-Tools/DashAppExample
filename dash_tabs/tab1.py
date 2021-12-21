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
    {'label': 'Input1', 'unit': '-', 'size_label': 'xl', 'ids': 'input1',
     'value': np.round(np.random.rand(), 2)}
input_2 = \
    {'label': 'Input2', 'unit': '', 'size_label': 'xl', 'ids': 'input2',
     'value': np.round(np.random.rand(), 2)}
input_3 = \
    {'label': 'Input3', 'unit': 'm', 'size_label': 'xl', 'ids': 'input3',
     'value': np.round(np.random.rand(), 2)}
input_4 = \
    {'label': 'Input4', 'unit': 'm²', 'size_label': 'xl', 'ids': 'input4',
     'value': np.round(np.random.rand(), 2)}
sub_frame1 = \
    {'children': 'Type: Input, Specifier: False',
     'className': 'title divider', 'size_label': 'xl',
     'widget_dicts': [input_1, input_2, input_3, input_4]}
input2 = \
    {'label': 'Input5', 'types': 'multiinput', 'size_label': 'l', 'unit': 'km',
     'value': np.round(np.random.rand(), 2), 'ids': 'input5', 'number': 2}
sub_frame2 = \
    {'children': 'Type: Input, Specifier: 1 Output Component with 2 Inputs',
     'className': 'title divider', 'size_label': 'l',
     'widget_dicts': [input2]}
label_inp3 = \
    {'widget': 'label', 'size_label': 's', 'value': ['Input A', 'Input B']}
input3 = \
    {'label': 'Input6', 'types': 'multiinput', 'size_label': 's', 'unit': 'm',
     'value': [[54, 54], [60, 60]], 'ids': [['input6a', [0, 1]],
                                            ['input6b', [2, 3]]], 'number': 4}
sub_frame3 = \
    {'children': 'Type: Input, Specifier: 2 Output Components with 4 Inputs',
     'className': 'title divider', 'size_label': 's',
     'widget_dicts': [label_inp3, input3]}

tab_dict = {'title': 'Tab1',
            'sub_frame_dicts': [sub_frame1, sub_frame2, sub_frame3]}


tab_layout = \
    html.Div(dl.frame(tab_dict), className='neat-spacing')

# print(tab_layout)
# @app.callback(
#