"""Main drawing functions
"""
import sys
from drawing import cmdparse, commands


@cmdparse.handle('Q', require_canvas=False)
def q(drawing):
    sys.exit(0)


@cmdparse.handle('C', int, int, require_canvas=False)
def c(w, h, drawing):
    return commands.canvas(w, h, drawing)


def render(drawing, width):
    pass


def draw(cmd, drawing):
    drawing = reduce(lambda x, fn: fn(cmd, x), [q, c], drawing)
    render(drawing, 20)

    return drawing
