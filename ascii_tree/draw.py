'''
Functions for drawing
'''
from typing import List
from .constants import PADDING
from .custom_types import Node, Offset


def draw_node(screen: list, text: str, left_bound: int, top_bound: int, box_width: int, line_width: int, padding: int=PADDING):
    '''
    Update screen buffer with node ascii repr
    '''
    row_idx = top_bound
    # inclusive left and right boundaries
    right_bound = left_bound + box_width

    # top border
    for i in range(left_bound, right_bound+1):
        screen[row_idx][i] = '-'

    # top padding
    row_idx += 1
    for p in range(padding):
        for i in range(left_bound, right_bound+1):
            if i == left_bound:
                screen[row_idx + p][i] = '|'
            elif i == right_bound:
                screen[row_idx + p][i] = '|'

    # create body of box
    # each row will contain box_width total characters
    # and line_width text chars
    row_idx += padding
    idx = 0  # iterates over chars in text
    while idx < len(text):
        # left boundary
        screen[row_idx][left_bound] = '|'
        # left padding
        for i in range(padding):
            screen[row_idx][left_bound + i + 1] = ' '
        # content
        subtext = text[idx:idx + line_width]
        text_lbound = left_bound + padding + 1
        screen[row_idx][text_lbound: text_lbound+len(subtext)] = subtext
        # right padding
        for i in range(padding):
            screen[row_idx][right_bound - i - 1] = ' '
        # right boundary
        screen[row_idx][right_bound] = '|'
        idx += line_width
        row_idx += 1

    # bottom padding
    for p in range(padding):
        for i in range(left_bound, right_bound+1):
            if i == left_bound:
                screen[row_idx + p][i] = '|'
            elif i == right_bound:
                screen[row_idx + p][i] = '|'

    row_idx += padding
    # bottom border
    for i in range(left_bound, right_bound +1):
        screen[row_idx][i] = '-'


def draw_edge(screen, src: Node, dest: Node):
    '''
    draw an edge between src and destination nodes.
    an edge always extends from the side/bottom of src node and goes to the
    middle of the of dest node
    '''
    ascii_src = src.box
    ascii_dest = dest.box
    # for dest, edge will connect in middle of top
    dest_x = ascii_dest.position.left + ascii_dest.box_width // 2
    dest_y = ascii_dest.position.top

    src_lbound = ascii_src.position.left
    src_rbound = ascii_src.position.left + ascii_src.box_width
    src_ymiddle = ascii_src.position.top + ascii_src.box_height // 2
    # based on entry point on dest, determine whether
    # the line will go from left, right, or center
    # of source

    if src_lbound > dest_x:
        # edge will go from left of source box
        # y-axis of where to extend from source
        # first draw horizontal leg
        for i in range(src_lbound, dest_x-1, -1):
            screen[src_ymiddle][i] = '-'
        # then draw vertical leg
        for i in range(src_ymiddle+1, dest_y):
            screen[i][dest_x] = '|'
    elif src_rbound < dest_x:
        # edge will go from right of source box
        for i in range(src_rbound, dest_x+1):
            screen[src_ymiddle][i] = '-'
        # then draw vertical leg
        for i in range(src_ymiddle+1, dest_y):
            screen[i][dest_x] = '|'
    else:
        # edge will go from underneath source box
        src_ybottom = ascii_src.box_height + ascii_src.position.top
        for i in range(src_ybottom, dest_y):
            screen[i][dest_x] = '|'


def draw(screen: List[List[str]], root: Node, padding: int=PADDING):
    '''
    traverse tree and draw nodes and edges
    '''
    stack = [root]
    while stack:
        node = stack.pop()
        left_bound, top_bound = node.box.position
        box_width, line_width = node.box.box_width, node.box.line_width
        draw_node(screen, node.val, left_bound, top_bound, box_width, line_width, padding)
        for child in node.children:
            # order doesn't matter since each node is drawn independently
            stack.append(child)
            draw_edge(screen, node, child)
