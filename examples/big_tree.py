'''
if the tree can't fit on one screen, it will be split into
pages and printed over multiple pages.
First let's construct a big tree.
'''
from ascii_tree import make_and_print_tree


class NTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

'''
First generate a really wide tree
'''

root0 = NTreeNode('onomatopaie'*10)
root0.children = [NTreeNode('boobar'), NTreeNode('car'), NTreeNode('scuba'), NTreeNode('tarzanman'), NTreeNode('smartcar')]
root0.children[-1].children = [NTreeNode('Kathmandu'), NTreeNode('smartcat '*20), NTreeNode('lorem ipsum dolor...')]
root0.children[-1].children[0].children = [NTreeNode('fooball '*10)]
root0.children[-1].children[1].children = [NTreeNode('foosbag')]
root0.children.append(NTreeNode('carbar'))
print("Printing root0...")
make_and_print_tree(root0, lambda node: node.val, lambda node:node.children)

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
Consider this tree.
'''

root2 = NTreeNode('onomatopaie'*10)
root2.children = [NTreeNode('boobar'), NTreeNode('car'), NTreeNode('scuba'), NTreeNode('tarzanman'), NTreeNode('smartcar')]
root2.children[-1].children = [NTreeNode('Kathmandu'*5), NTreeNode('smartcat '*20), NTreeNode('lorem ipsum dolor...'*20)]
root2.children[-1].children.extend([NTreeNode('Kathmandu'*5), NTreeNode('smartcat '*20), NTreeNode('lorem ipsum dolor...'*20)])
root2.children[-1].children[0].children = [NTreeNode('fooball '*10)]
root2.children[-1].children[1].children = [NTreeNode('foosbag')]
root2.children.append(NTreeNode('carbar'))
print("Printing root2...")
make_and_print_tree(root2, lambda node: node.val, lambda node:node.children)
