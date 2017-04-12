"""Draw stuff
"""
import itertools


def pos(x, y, w, h):
    return x + y * w


def canvas(width, height, drawing):
    return " " * (width * height)


def line(x1, y1, x2, y2, w, h, drawing):
    dx, dy = range(x1 - 1, x2), range(y1 - 1, y2)

    if len(dx) > 1 and len(dy) > 1:
        raise ValueError

    def draw(d, xy):
        x, y = xy
        l = list(d)
        l[pos(x, y, w, h)] = "x"
        return "".join(l)

    return reduce(draw, itertools.product(dx, dy), drawing)


def rect(x1, y1, x2, y2, drawing):
    raise NotImplementedError


def fill(x, y, coler, drawing):
    raise NotImplementedError
