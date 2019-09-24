from ascii_tree import make_and_print_tree, update_param
from node_types import NTreeNode

root = NTreeNode('Lorem ipsum dolor sit amet')
root.children = [NTreeNode('consectetur adipiscing elit.'), NTreeNode('Etiam laoreet congue')]
root.children[0].children = [NTreeNode('Pellentesque finibus metus eget'), NTreeNode('ante aliquet ullamcorper')]
root.children[1].children = [NTreeNode('Morbi porta, diam at imperdiet venenatis'),  NTreeNode('neque eros bibendum tortor, quis')]

update_param('screen_width', 120)
update_param('box_max_width', 20)
update_param('charset', 'ascii')
make_and_print_tree(root, lambda n: n.val, lambda n:n.children)
