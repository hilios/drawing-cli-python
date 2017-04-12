"""Draw stuff in the canvas.

All X and Y coordinates are zero-based positions relative to the canvas.
"""
import itertools


def to_index(x, y, w, h):
    "Converts an 2D coordinate to an linear index, not allowing out of bounds"
    _x = abs(x) if x < w else w - 1
    _y = abs(y) if y < h else h - 1
    return _x + _y * w


def fill(x, y, f, w, h, drawing):
    "Fills an coordinate with given filler"
    i = to_index(x, y, w, h)
    return "%s%s%s" % (drawing[:i], f, drawing[i+1:])


def canvas(width, height, drawing):
    return " " * (width * height)


def line(x1, y1, x2, y2, w, h, drawing):
    dx, dy = range(x1, x2 + 1), range(y1, y2 + 1)

    if len(dx) > 1 and len(dy) > 1:
        raise ValueError

    return reduce(lambda d, xy: fill(*xy, f='x', w=w, h=h, drawing=d),
        itertools.product(dx, dy), drawing)


def rect(x1, y1, x2, y2, w, h, drawing):
    t = (x1, y1, x2, y1)
    r = (x2, y1, x2, y2)
    b = (x1, y2, x2, y2)
    l = (x1, y1, x1, y2)
    return reduce(lambda d, largs: line(*largs,
        w=w, h=h, drawing=d), (t,r,b,l), drawing)


def bucket(x, y, c, w, h, drawing):
    return fill(x, y, c, w, h, drawing)
