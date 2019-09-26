'''
Utilities for external interactions
'''
from . import charsets
from typing import Callable, Any, List
from .ascii_tree import print_tree
from .custom_types import Node


# params may overlap
SCREEN_PARAM_NAMES = ['screen_width', 'margin', 'padding', 'charset']
BOX_PARAM_NAMES = ['padding', 'box_max_width']
# updated param values
_screen_params = {}
_box_params = {}


def transformed_tree(root: Any, get_val: Callable[[Any], Any], get_children: Callable[[Any], List])->Node:
    '''
    Utility func
    transform tree from arbitrary node type
    to tree of `Node`. This is needed since
    functions here assume the Node structure.
    `get_val` and `get_children` are callables that when called
    on source node, return val and children (list) respectively.
    '''
    troot = Node.init_with_box(get_val(root), **_box_params)
    troot.children = [transformed_tree(child, get_val, get_children) for child in get_children(root)]
    return troot


def make_and_print_tree(root: Any, get_val: Callable[[Any], Any], get_children: Callable[[Any], List]):
    '''
    Utility method that transforms and prints tree(s)
    '''
    print_tree(transformed_tree(root, get_val, get_children), **_screen_params)


def transform_param(param, val):
    '''
    some param value need to be transformed
    '''
    if param == 'charset':
        if val.lower() == 'unicode':
            return charsets.Unicode
        return charsets.Ascii

    return val


def update_param(param: str, new_val):
    '''
    updates param dict
    '''
    param = param.lower()
    new_val = transform_param(param, new_val)
    if param in SCREEN_PARAM_NAMES:
        _screen_params[param] = new_val
        print(f'{param} updated to {new_val}')
    if param in BOX_PARAM_NAMES:
        _box_params[param] = new_val
        print(f'{param} updated to {new_val}')
