'''
Ascii Tree is library for printing beautiful ascii trees.
The first step is to convert the tree into another
tree that is comrehensible by the library.
For this we'll use the following.
'''

from ascii_tree import transformed_tree, print_tree
from node_types import BinaryTreeNode


'''
construct a dummy tre
'''
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

'''
transformed_tree(root, get_val: Callable, get_children: Callable):
transformed_tree accepts the root node of some arbitrary tree class,
a callable, called with the node as the argument to get its value
and another callable to get the current node's children
'''

def get_val(node):
    '''
    get value from node
    '''
    return node.value


def get_children(node):
    '''
    get list of children from node
    '''
    children = []
    if node.left:
        children.append(node.left)
    if node.right:
        children.append(node.right)
    return children


troot = transformed_tree(root, get_val, get_children)
print_tree(troot)
'''
page: 0
          ------
          |    |
       ---- 1  -------------
       |  |    |           |
       |  ------           |
       |                   |
       |                   |
       |                   |
       |                   |
       |                   |
     ------              ------
     |    |              |    |
  ---- 2  ---         ---- 3  ---
  |  |    | |         |  |    | |
  |  ------ |         |  ------ |
  |         |         |         |
  |         |         |         |
  |         |         |         |
  |         |         |         |
  |         |         |         |
------    ------    ------    ------
|    |    |    |    |    |    |    |
| 4  |    | 5  |    | 6  |    | 7  |
|    |    |    |    |    |    |    |
------    ------    ------    ------
'''
