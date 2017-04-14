"""Parses and apply a drawing command to some canvas.

All X, Y coordinates are one-based positions relative to the canvas width and
height.
"""
import sys
from drawing import canvas, cmdparse
from drawing.canvas import blank_canvas


@cmdparse.handle('Q', require_canvas=False)
def q(*args, **kwargs):
    sys.exit(0)


@cmdparse.handle('C', int, int, require_canvas=False)
def c(w, h, canvas):
    return blank_canvas(w, h)


@cmdparse.handle('L', int, int, int, int)
def l(x1, y1, x2, y2, canvas):
    return canvas.line(x1-1, y1-1, x2-1, y2-1)


@cmdparse.handle('R', int, int, int, int)
def r(x1, y1, x2, y2, canvas):
    return canvas.rect(x1-1, y1-1, x2-1, y2-1)


@cmdparse.handle('B', int, int, str)
def b(x, y, colour, canvas):
    return canvas.bucket(x-1, y-1, colour)


def render(cmd, canvas):
    new_canvas = reduce(lambda x, fn: fn(cmd, x), [q, c, l, r, b], canvas)
    if new_canvas:
        print new_canvas.render()
    return new_canvas
