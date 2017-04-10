"""Drawing actions and constraints
"""
import sys
from drawing.cmdparse import action


@action("Q", require_canvas=False)
def quit(cmd, drawing):
    sys.exit(0)


@action("C", require_canvas=False)
def canvas(cmd, drawing):
    _, width, height = cmd
    drawing = " " * (int(width) * int(height))


@action("L")
def line(cmd, drawing):
    _, x1, y1, x2, y2 = cmd
