import math
from collections import namedtuple, deque
from copy import copy
from .params import PADDING, BOX_MAX_WIDTH

# position offset
Offset = namedtuple('Offset', 'left top')


class Node:
    '''
    Representing a node of the user tree
    '''
    def __init__(self, val):
        self.val = str(val)
        self.children = deque()
        # reference to its AsciiBox
        self.box = None

    @classmethod
    def init_with_box(cls, val, **kwargs):
        '''
        construct Node with associated AsciiBox
        accepts kwargs to be passed to AsciiBox constructor
        '''
        node = cls(val)
        node.box = AsciiBox(node.val, **kwargs)
        return node

    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val

    @property
    def is_leaf(self):
        return len(self.children) == 0

    def __copy__(self):
        '''
        utility to make a copy with
        box copied and empty children
        '''
        clone = Node(self.val)
        clone.box = copy(self.box)
        return clone


class AsciiBox:
    '''
    Holds parameters associated with drawing
    ascii box containing some text.
    '''
    def __init__(self, text: str, box_max_width: int=BOX_MAX_WIDTH, padding: int=PADDING):
        self.text = text
        # width of encapsulating box (includes border chars)
        self.box_width = None
        # numbers of chars line of text
        self.line_width = None
        # height of box
        self.box_height = None
        # height of contents
        self.content_height = None
        self.box_width, self.line_width, self.box_height, self.content_height = \
            self.box_dims(text, box_max_width, padding)
        # width of tree rooted at node
        # this must be updated for non-leaf nodes
        self.tree_width = self.box_width
        # top-left corner of this box's position
        self.position = None
        # left-offset of tree rooted at this node
        # i.e. the left offset of rectangular box
        # consumed by this node and it's descendents.
        self.tree_left_offset = None

    def __repr__(self):
        return f'[{self.text}](bw:{self.box_width}, bh:{self.box_height}, cw:{self.line_width}, ch:{self.content_height})'

    @property
    def width(self):
        return self.box_width

    def box_dims(self, text: str, box_max_width: int, padding: int):
        '''
        determine the box dimensions, i.e.
        box_width (width including border chars)
        line_width (number of text chars)
        box_height (height including border chars)
        content_height (lines of wrapped text)
        '''
        # max text per line; each line has 2 paddings and 2 border chars
        max_line_width = box_max_width - 2*padding - 2
        if  max_line_width >= len(text):
            box_width = len(text) + 2*padding + 2
            line_width = len(text)
        else:
            # entire text won't fit on one line; wrap
            box_width = box_max_width
            line_width = max_line_width

        content_height = math.ceil(len(text) / line_width)
        # box height is height of content + 2 paddings + 2 border chars
        box_height = content_height + 2*padding + 2

        return box_width, line_width, box_height, content_height
