Ascii Tree
==========

Generate beautiful ascii trees.

Installation
============
`git clone ...`

`cd ...`

`python3 setup.py install`

Usage
=====
This library can print **arbitrary** trees. This requires
you to specify how the value of a node, and list
of it's children can be extracted from the node object.
For example, consider the following binary tree node class
```
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

```
We can extract it's value and children like

```
def get_value(node):
    return node.value

def get_children(node):
    children = []
    if node.left:
        children.append(node.left)
    if node.right:
        children.append(node.right)
    return children
```
First we'll construct a dummy tree.
```
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
```
Now we can print this as an ascii tree like
```
>>> from ascii_tree import make_and_print_tree
>>> make_and_print_tree(root, get_value, get_children)
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
```

Currently the screen width (the maximum character width assumed by the tree) is `180`.
This can be updated like:
```
>>> from ascii_tree import update_param
>>> update_param('screen_width', 120)
>>> make_and_print_tree(root, get_value, get_children)
```

These params can be updated thus: `screen_width`, `margin` (distance between nodes),
`padding` (distance between box contents and border) and `box_max_width`.

See more examples [here](./examples)

Notes
=====
- Only supports `python3`

- Boxes/nodes can have be upto max width, beyond which
their contents are wrapped.

- If a tree is too wide, then it is split at a node.
Practically, this means that some children go one side
of the split, and the rest on the other side.
When a node is split, an information box is added as
a child to the node, which shows the page number where tree is continued.

