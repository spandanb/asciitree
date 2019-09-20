'''
Utilities for external interactions
'''
from typing import Callable
from .custom_types import Node


def transformed_tree(root, get_val: Callable, get_children: Callable):
    '''
    Utility func
    transform tree from arbitrary node type
    to tree of `Node`. This is needed since
    functions here assume the Node structure.
    `get_val` and `get_children` are callables that when called
    on source node, return val and children respectively.
    '''
    troot = Node(get_val(root))
    troot.children = [transformed_tree(child, get_val, get_children) for child in get_children(root)]
    return troot
