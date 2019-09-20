'''
Utilities for external interactions
'''
from typing import Callable, Any, List
from .ascii_tree import print_tree
from .custom_types import Node


def transformed_tree(root: Any, get_val: Callable[[Any], Any], get_children: Callable[[Any], List])->Node:
    '''
    Utility func
    transform tree from arbitrary node type
    to tree of `Node`. This is needed since
    functions here assume the Node structure.
    `get_val` and `get_children` are callables that when called
    on source node, return val and children (list) respectively.
    '''
    troot = Node(get_val(root))
    troot.children = [transformed_tree(child, get_val, get_children) for child in get_children(root)]
    return troot


def make_and_print_tree(root: Any, get_val: Callable[[Any], Any], get_children: Callable[[Any], List]):
    '''
    Utility method that transforms and prints tree
    '''
    print_tree(transformed_tree(root, get_val, get_children))

