from ascii_tree import make_and_print_tree
from node_types import  NTreeNode

'''
Now make it ever wider, such that it can't fit on the screen.
This will print multiple pages now
'''
root1 = NTreeNode('onomatopaie'*10)
root1.children = [NTreeNode(f'lorem ipsum dolor...{i}') for i in range(10)]
print("Printing root1...")
make_and_print_tree(root1, lambda node: node.val, lambda node:node.children)

'''
Notice how the object is split over multiple pages.
Also observer that the parent is duplicated in both pages.
This is done to make the graph more readable.
The splitting algorithm will split along any level of
the tree.
'''
