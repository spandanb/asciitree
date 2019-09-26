'''
different characters to draw the ascii tree with
'''

class Charset:
    def __init__(self, name=None, xside=None, yside=None, top=None, bottom=None, left=None, right=None,
                 top_left=None, top_right=None, bottom_left=None, bottom_right=None, top_out=None,
                 bottom_out=None, left_out=None, right_out=None):
        '''
        Accepts characters for different elements of the box.
        Minimally, (xside, yside) or (top, left, bottom, right)
        must be specified. The rest are intended to allow finer control.

        xside: character to use for top and bottom, i.e. along x-axis
        yside: character to use for left and right, i.e. along y-axis
        top: character to use for box top. defaults to xside
        bottom:
        left: character to use for box left. defaults to yside
        right:
        top_left: character to use for top-left corner. defaults to xside
        top_right:
        bottom_left:
        bottom_right:
        left_out: character where an edge connects on the left. defaults to yside
        right_out:
        top_out: character where an edge connects on the left. defaults to xside
        bottom_out:
        '''
        if (xside is None or yside is None) and \
           (left is None or right is None or top is None or bottom is None):
            raise ValueError('Underdefined character set')

        self.name = str(name)
        self.xside = xside or top
        self.yside = yside or left
        self.top = top or xside
        self.bottom = bottom or xside
        self.left = left or yside
        self.right = right or yside

        self.top_left = top_left or xside
        self.top_right = top_right or xside
        self.bottom_left = bottom_left or xside
        self.bottom_right = bottom_right or xside
        self.top_out = top_out or xside
        self.bottom_out = bottom_out or xside
        self.left_out = left_out or yside
        self.right_out = right_out or yside

    def __str__(self):
        return self.name

Ascii = Charset(name='ascii', xside='-', yside='|')
Unicode = Charset(name='unicode', xside='─', yside='│', top_left='┌', top_right='┐', bottom_left='└', bottom_right='┘',
                  left_out='┤', right_out='├', top_out='┴', bottom_out='┬')
