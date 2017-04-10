"""Draw stuff
"""


def canvas(width, height, drawing):
    return " " * (width * height)


def line(x1, y1, x2, y2, drawing):
    raise NotImplementedError


def rect(x1, y1, x2, y2, drawing):
    raise NotImplementedError


def fill(x, y, coler, drawing):
    raise NotImplementedError
