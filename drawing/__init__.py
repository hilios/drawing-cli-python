"""Main drawing functions
"""
import sys
import re
from drawing import cmdparse, draw


@cmdparse.handle('Q', require_canvas=False)
def q(drawing):
    sys.exit(0)


@cmdparse.handle('C', int, int, require_canvas=False)
def c(w, h, drawing):
    return "%s\t%d\t%d" % (draw.canvas(w, h, drawing), w, h)


@cmdparse.handle('L', int, int, int, int)
def l(x1, y1, x2, y2, drawing):
    return draw.line(x1, y1, x2, y2, drawing)


@cmdparse.handle('R', int, int, int, int)
def r(x1, y1, x2, y2, drawing):
    return draw.rect(x1, y1, x2, y2, drawing)


@cmdparse.handle('B', int, int, str)
def b(x1, y1, c, drawing):
    return draw.fill(x1, y1, c, drawing)


def lines(width, data, lines=[]):
    head, tail = data[0:width], data[width:]
    if tail:
        lines(width, tail, [head] + lines)


def render(cmd, drawing):
    drawing = reduce(lambda x, fn: fn(cmd, x), [q, c, l, r, b], drawing)

    if drawing:
        d, w, h = drawing.split("\t")
        width, height = int(w), int(h)
        print "\n".join(
            ["+{header}+"] +
            ["|%s|" % d[(i * width):(i * width + width)] for i in xrange(height)] +
            ["+{footer}+"]
        ).format(header="-" * width, footer="-" * width)

    return drawing
