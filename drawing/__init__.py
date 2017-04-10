"""Main drawing functions
"""
import sys
from drawing import cmdparse, render


@cmdparse.handle('Q', require_canvas=False)
def q(drawing):
    sys.exit(0)


@cmdparse.handle('C', int, int)
def c(w, h, drawing):
    return render.canvas(w, h, drawing)


def render(drawing, width):
    pass


def draw(cmd, drawing):
    drawing = reduce(lambda fn, draw: fn(cmd, draw), [q, c,])
    render(drawing, 20)

    return drawing
