import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from functools import wraps
from flask_caching import Cache
import base64
import io
import json
import copy
import collections
from glom import glom


def tab_container(child, label, ids):
    tabs = dcc.Tabs(
        [dcc.Tab(child[_], label=label_id, value=tab_id, className='custom-tab',
                 selected_className='custom-tab-selected')
         for _, (label_id, tab_id) in enumerate(zip(label, ids))],
        id='tabs', parent_className='some_container', value=ids[0],
        className='custom-tabs')
    return tabs


def val_container(ids, types='output', specifier=False):
    inputs = [html.Div(
        [html.Div(id={'type': types, 'id': cont_id,
                      'specifier': f'{specifier}_children'},
                  className='gd-desc centered'),
         html.Div(id={'type': types, 'id': cont_id,
                      'specifier': f'{specifier}_value'},
                  className='value'),
         html.Div(id={'type': types, 'id': cont_id,
                      'specifier': f'{specifier}_unit'},
                  className='unit')],
        id={'type': types, 'id': cont_id,
            'specifier': f'{specifier}_container'},
        className='val_container') for cont_id in ids]
    return inputs


def spacing(label, unit):
    """
    label: xs=33%, s=38%, m=45%, l=50%, xl=70%
    unit: s=5%, m=12%
    {n:name, p:percentage}
    """
    spacing_label = {'xs': {'n': 'label-param-s', 'p': 33},
                     's': {'n': 'label-param', 'p': 38},
                     'm': {'n': 'label-param-m', 'p': 45},
                     'l': {'n': 'label-param-l', 'p': 50},
                     'xl': {'n': 'label-param-xl', 'p': 70}, }
    spacing_unit = {'s': {'n': 'ufontm centered', 'p': 5},
                    'm': {'n': 'ufont centered', 'p': 12}}

    return spacing_label[label], spacing_unit[unit]


def checklist(checked):
    return [] if checked is False else [1]


def type_input(comp_type, check_val, **kwargs):
    if comp_type == 'input':
        return dbc.Input(**kwargs)
    elif comp_type == 'dropdown':
        return dcc.Dropdown(**kwargs)
    elif comp_type == 'checklist':
        return dcc.Checklist(**kwargs)
    elif comp_type == 'label':
        label = list(check_val) if isinstance(check_val, str) else check_val
        l_out = [dbc.Col(html.Div(lab), className='sm-label') for lab in label]
        return l_out
    else:
        raise NotImplementedError('Type of Component not implemented')


def row_input(label='', ids='', value='', widget='input', unit='', options='',
              activated=False, size_label='s', size_unit='s', types='input',
              specifier=False, disabled=False,  **kwargs):
    """
    label: str; ids: str/list of strs for each input ids; value: int/float;
    widget: checklist, dropdown, or label, if not set then input will be set;
    unit: str type, set if unit is used; options:only for dropdown;
    activated:only for checklist, True if checklist is prechecked;
    size_label, size_unit: str type for spacing (see def spacing() );
    types: str type (input/output), input if not set (trial);
    specifier: id callback more specific, usually widget is set as specifier,
    but more specific specifier can be initialised
    """
    id_list = [ids] if not isinstance(ids, list) else ids
    new_val = [value] if not isinstance(value, list) else value
    # val_list = []
    if len(new_val) != len(id_list):
        val_list = new_val * len(id_list)
    else:
        val_list = new_val

    s_label, s_unit = spacing(size_label, size_unit)
    p_input = 100-(s_label['p']+s_unit['p'])
    s_input = {'width': f'{p_input}%'}

    if widget == 'input':
        children = \
            [dbc.Input(
                id={'type': types, 'id': input_id, 'specifier': specifier},
                persistence=True, persistence_type="memory", value=val,
                debounce=True, className='val_input', disabled=disabled,
                **kwargs) for input_id, val in zip(id_list, val_list)]
    elif widget == 'dropdown':
        children = \
            [dbc.Col(dcc.Dropdown(
                id={'type': types, 'id': input_id, 'specifier': specifier},
                options=options, value=value, persistence=True,
                persistence_type="memory", clearable=False, disabled=disabled,
                className='input-style-dropdown')) for input_id in id_list]
    elif widget == 'checklist':
        children = [dbc.Col(dbc.Checklist(
            options=[{"label": "", "value": 1}], value=checklist(activated),
            id={"type": types, "id": input_id, 'specifier': specifier},
            inline=True, persistence=True, persistence_type="memory",
            disabled=disabled, className='checklist')) for input_id in id_list]

    elif widget == 'label':
        new_label = list(value) if isinstance(value, str) else value
        children = [dbc.Col(html.Div(label), className='sm-label') for label in
                    new_label]
    else:
        raise NotImplementedError('Type of Component not implemented')

    if not isinstance(ids, list) and specifier == 'visibility':
        id_container = \
            {'type': 'container', 'id': ids, 'specifier': 'visibility'}
        inputs = html.Div(
            [dbc.Label(label, className=s_label['n'] + ' g-0'),
             html.Div(children, className='centered r_flex g-0', style=s_input),
             html.Div(unit, className=s_unit['n'] + ' g-0')], id=id_container,
            className="row-lay r_flex g-0")
    else:
        inputs = html.Div(
            [dbc.Label(label, className=s_label['n'] + ' g-0'),
             html.Div(children, className='centered r_flex g-0', style=s_input),
             html.Div(unit, className=s_unit['n'] + ' g-0')],
            className="row-lay r_flex g-0")

    return inputs


