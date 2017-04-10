"""Main drawing functions
"""
import sys
from drawing import cmdparse, draw


@cmdparse.handle('Q', require_canvas=False)
def q(drawing):
    sys.exit(0)


@cmdparse.handle('C', int, int, require_canvas=False)
def c(w, h, drawing):
    return draw.canvas(w, h, drawing)


@cmdparse.handle('L', int, int, int, int)
def l(x1, y1, x2, y2, drawing):
    return draw.line(x1, y1, x2, y2, drawing)


@cmdparse.handle('R', int, int, int, int)
def r(x1, y1, x2, y2, drawing):
    return draw.rect(x1, y1, x2, y2, drawing)


@cmdparse.handle('B', int, int, str)
def b(x1, y1, c, drawing):
    return draw.fill(x1, y1, c, drawing)


def render(cmd, drawing):
    drawing = reduce(lambda x, fn: fn(cmd, x), [q, c, l, r, b], drawing)

    return drawing
