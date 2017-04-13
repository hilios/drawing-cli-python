"""Parses and apply a drawing command to some canvas.

All X, Y coordinates are one-based positions relative to the canvas width and
height.
"""
import sys
from drawing import cmdparse, draw, utils


@cmdparse.handle('Q', require_canvas=False)
def q(*args, **kwargs):
    sys.exit(0)


@cmdparse.handle('C', int, int, require_canvas=False)
def c(w, h, canvas):
    return (w, h, draw.canvas(w, h, None))


@cmdparse.handle('L', int, int, int, int)
def l(x1, y1, x2, y2, canvas):
    w, h, drawing = canvas
    return (w, h, draw.line(x1-1, y1-1, x2-1, y2-1, w, h, drawing))


@cmdparse.handle('R', int, int, int, int)
def r(x1, y1, x2, y2, canvas):
    w, h, drawing = canvas
    return (w, h, draw.rect(x1-1, y1-1, x2-1, y2-1, w, h, drawing))


@cmdparse.handle('B', int, int, str)
def b(x, y, colour, canvas):
    w, h, drawing = canvas
    return (w, h, draw.bucket(x-1, y-1, colour, w, h, drawing))


def render(cmd, canvas):
    new_canvas = reduce(lambda x, fn: fn(cmd, x), [q, c, l, r, b], canvas)
    if new_canvas:
        print utils.pretty_render(*new_canvas)
    return new_canvas
