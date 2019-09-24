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
For example, consider the following n-ary tree node class
```
>>> class NTreeNode:
...    def __init__(self, val):
...        self.val = val
...        self.children = []
```
We can extract it's value and children like

```
>>> def get_value(node):
...     return node.value
...
>>> def get_children(node):
...     return node.children
...
```
First, we'll construct a dummy tree.
```
>>> root = NTreeNode('Lorem ipsum dolor sit amet')
>>> root.children = [NTreeNode('consectetur adipiscing elit.'), NTreeNode('Etiam laoreet congue')]
>>> root.children[0].children = [NTreeNode('Pellentesque finibus metus eget'), NTreeNode('ante aliquet ullamcorper')]
>>> root.children[1].children = [NTreeNode('Morbi porta, diam at imperdiet venenatis'),  NTreeNode('neque eros bibendum tortor, quis')]
```
Now we can print this as an ascii tree like
```
>>> from ascii_tree import make_and_print_tree
>>> make_and_print_tree(root, get_value, get_children)
page: 0
                            ┌───────────────────┐                                                                       
                            │                   │                                                                       
                            │ Lorem ipsum dolo  │                                                                       
                            │ r sit amet        ├────────────────────────────────────┐                                  
                            │                   │                                    │                                  
                            └┬──────────────────┘                                    │                                  
                             │                                                       │                                  
                             │                                                       │                                  
                             │                                                       │                                  
                             │                                                       │                                  
                             │                                                       │                                  
                   ┌─────────┴─────────┐                                   ┌─────────┴─────────┐                        
                   │                   │                                   │                   │                        
                   │ consectetur adip  │                                   │ Etiam laoreet co  │                        
                   │ iscing elit.      ├────────────────────┐              │ ngue              │                        
                   │                   │                    │              │                   │                        
                   └──┬────────────────┘                    │              └───────────────────┘                        
                      │                                     │                                                           
                      │                                     │                                                           
                      │                                     │                                                           
                      │                                     │                                                           
                      │                                     │                                                           
            ┌─────────┴─────────┐                 ┌─────────┴─────────┐                                                 
            │                   │                 │                   │                                                 
            │ Pellentesque fin  │                 │ ante aliquet ull  │                                                 
          ┌─┤ ibus metus eget   ├──┐              │ amcorper          │                                                 
          │ │                   │  │              │                   │                                                 
          │ └───────────────────┘  │              └───────────────────┘                                                 
          │                        │                                                                                    
          │                        │                                                                                    
          │                        │                                                                                    
          │                        │                                                                                    
          │                        │                                                                                    
┌─────────┴─────────┐    ┌─────────┴─────────┐                                                                          
│                   │    │                   │                                                                          
│ Sed nec nibh cur  │    │ volutpat lacus a  │                                                                          
│ sus               │    │ t, euismod mi     │                                                                          
│                   │    │                   │                                                                          
└───────────────────┘    └───────────────────┘                                                                          
```
We can also print the tree using only ascii characters like:
```
>>> update_param('charset', 'ascii')
>>> make_and_print_tree(root, lambda n: n.val, lambda n: n.children)
page: 0
                            ---------------------                                                                       
                            |                   |                                                                       
                            | Lorem ipsum dolo  |                                                                       
                            | r sit amet        |-------------------------------------                                  
                            |                   |                                    |                                  
                            ---------------------                                    |                                  
                             |                                                       |                                  
                             |                                                       |                                  
                             |                                                       |                                  
                             |                                                       |                                  
                             |                                                       |                                  
                   ---------------------                                   ---------------------                        
                   |                   |                                   |                   |                        
                   | consectetur adip  |                                   | Etiam laoreet co  |                        
                   | iscing elit.      |---------------------              | ngue              |                        
                   |                   |                    |              |                   |                        
                   ---------------------                    |              ---------------------                        
                      |                                     |                                                           
                      |                                     |                                                           
                      |                                     |                                                           
                      |                                     |                                                           
                      |                                     |                                                           
            ---------------------                 ---------------------                                                 
            |                   |                 |                   |                                                 
            | Pellentesque fin  |                 | ante aliquet ull  |                                                 
          --| ibus metus eget   |---              | amcorper          |                                                 
          | |                   |  |              |                   |                                                 
          | ---------------------  |              ---------------------                                                 
          |                        |                                                                                    
          |                        |                                                                                    
          |                        |                                                                                    
          |                        |                                                                                    
          |                        |                                                                                    
---------------------    ---------------------                                                                          
|                   |    |                   |                                                                          
| Sed nec nibh cur  |    | volutpat lacus a  |                                                                          
| sus               |    | t, euismod mi     |                                                                          
|                   |    |                   |                                                                          
---------------------    ---------------------                                                                          
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

See more examples [here](./examples).

The [call_graph](https://github.com/spandanb/call_graph) library uses `ascii_tree` to print call graphs.

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

