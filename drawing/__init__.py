"""Main drawing functions
"""
import sys
from drawing import cmdparse, draw, utils


@cmdparse.handle('Q', require_canvas=False)
def q(*args):
    sys.exit(0)


@cmdparse.handle('C', int, int, require_canvas=False)
def c(w, h, canvas):
    return (w, h, draw.canvas(w, h, None))


@cmdparse.handle('L', int, int, int, int)
def l(x1, y1, x2, y2, canvas):
    w, h, drawing = canvas
    return (w, h, draw.line(w, h, x1, y1, x2, y2, drawing))


@cmdparse.handle('R', int, int, int, int)
def r(x1, y1, x2, y2, canvas):
    w, h, drawing = canvas
    return (w, h, draw.rect(x1, y1, x2, y2, drawing))


@cmdparse.handle('B', int, int, str)
def b(x1, y1, c, canvas):
    w, h, drawing = canvas
    return (w, h, draw.fill(x1, y1, c, drawing))


def render(cmd, canvas):
    new_canvas = reduce(lambda x, fn: fn(cmd, x), [q, c, l, r, b], canvas)
    print utils.pretty_render(*new_canvas)
    return new_canvas
