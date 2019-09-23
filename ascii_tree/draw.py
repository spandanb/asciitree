'''
Functions for drawing
'''
from . import charsets
from typing import List
from .params import PADDING
from .custom_types import Node, Offset


def draw_node(screen: list, text: str, left_bound: int, top_bound: int, box_width: int,
              line_width: int, padding: int=PADDING, charset=charsets.Ascii):
    '''
    Update screen buffer with node ascii repr
    '''
    # inclusive left and right boundaries
    right_bound = left_bound + box_width

    # top border
    for i in range(left_bound+1, right_bound):
        screen[top_bound][i] = charset.top
    # top-left corner
    screen[top_bound][left_bound] = charset.top_left
    # top-right corner
    screen[top_bound][right_bound] = charset.top_right

    # top padding
    row_idx = top_bound + 1
    for p in range(padding):
        for i in range(left_bound, right_bound+1):
            if i == left_bound:
                screen[row_idx + p][i] = charset.left
            elif i == right_bound:
                screen[row_idx + p][i] = charset.right

    # create body of box
    # each row will contain box_width total characters
    # and line_width text chars
    row_idx += padding
    idx = 0  # iterates over chars in text
    while idx < len(text):
        # left boundary
        screen[row_idx][left_bound] = charset.left
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
        screen[row_idx][right_bound] = charset.right
        idx += line_width
        row_idx += 1

    # bottom padding
    for p in range(padding):
        for i in range(left_bound, right_bound+1):
            if i == left_bound:
                screen[row_idx + p][i] = charset.left
            elif i == right_bound:
                screen[row_idx + p][i] = charset.right

    row_idx += padding

    bottom_bound = row_idx
    # bottom-left corner
    screen[bottom_bound][left_bound] = charset.bottom_left
    # bottom-right corner
    screen[bottom_bound][right_bound] = charset.bottom_right
    # bottom border
    for i in range(left_bound+1, right_bound):
        screen[bottom_bound][i] = charset.bottom


def draw_edge(screen, src: Node, dest: Node, charset=charsets.Ascii):
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
        # draw horizontal leg
        for i in range(src_lbound, dest_x-1, -1):
            screen[src_ymiddle][i] = charset.xside
        # draw left out going portrusion
        screen[src_ymiddle][src_lbound] = charset.left_out
        # draw elbow of edge
        screen[src_ymiddle][dest_x] = charset.top_left
        # draw vertical leg
        for i in range(src_ymiddle+1, dest_y):
            screen[i][dest_x] = charset.yside
    elif src_rbound < dest_x:
        # edge will go from right of source box
        for i in range(src_rbound, dest_x+1):
            screen[src_ymiddle][i] = charset.xside
        # right protrusion
        screen[src_ymiddle][src_rbound] = charset.right_out
        # elbow
        screen[src_ymiddle][dest_x] = charset.top_right
        # then draw vertical leg
        for i in range(src_ymiddle+1, dest_y):
            screen[i][dest_x] = charset.yside
    else:
        # edge will go from underneath source box
        src_ybottom = ascii_src.box_height + ascii_src.position.top
        for i in range(src_ybottom, dest_y):
            screen[i][dest_x] = charset.yside
        # bottom protrusion - goes on box which is one unit
        # higher hence -1
        screen[src_ybottom-1][dest_x] = charset.bottom_out

    # every dest box will have a top out
    screen[dest_y][dest_x] = charset.top_out


def draw(screen: List[List[str]], root: Node, padding: int=PADDING, charset=charsets.Unicode):
    '''
    traverse tree and draw nodes and edges
    '''
    stack = [root]
    edges = []
    while stack:
        node = stack.pop()
        left_bound, top_bound = node.box.position
        box_width, line_width = node.box.box_width, node.box.line_width
        draw_node(screen, node.val, left_bound, top_bound, box_width, line_width, padding, charset)
        for child in node.children:
            # order doesn't matter since each node is drawn independently
            stack.append(child)
            edges.append((node, child))
    # draw edges at the end since draw_edge handles
    # adding outgoing protrusion chars on box
    for node, child in edges:
        draw_edge(screen, node, child, charset)
