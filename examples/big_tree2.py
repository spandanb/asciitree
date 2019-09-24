from ascii_tree import make_and_print_tree
from node_types import NTreeNode

root2 = NTreeNode('onomatopaie'*10)
root2.children = [NTreeNode('boobar'), NTreeNode('car'), NTreeNode('scuba'), NTreeNode('tarzanman'), NTreeNode('smartcar')]
root2.children[-1].children = [NTreeNode('Kathmandu'*5), NTreeNode('smartcat '*20), NTreeNode('lorem ipsum dolor...'*20)]
root2.children[-1].children.extend([NTreeNode('Kathmandu'*5), NTreeNode('smartcat '*20), NTreeNode('lorem ipsum dolor...'*20)])
root2.children[-1].children[0].children = [NTreeNode('fooball '*10)]
root2.children[-1].children[1].children = [NTreeNode('foosbag')]
root2.children.append(NTreeNode('carbar'))
print("Printing root2...")
make_and_print_tree(root2, lambda node: node.val, lambda node:node.children)
