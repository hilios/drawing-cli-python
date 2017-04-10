"""Helper methods
"""
from drawing  import cmdparse
from drawing.actions import quit, canvas


def render(drawing, width):
    pass


def draw(cmd, drawing):
    drawing = reduce(lambda fn, draw: fn(cmd, draw), [quit, canvas,])
    render(drawing, 20)

    return drawing
