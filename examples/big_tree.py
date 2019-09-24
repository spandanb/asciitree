'''
If the tree can't fit on one screen, it will be split into
pages and printed over multiple pages.
First let's construct a big tree.
'''
from ascii_tree import make_and_print_tree
from node_types import NTreeNode


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
