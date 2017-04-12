"""Draw stuff in the canvas.

All X and Y coordinates are zero-based positions relative to the canvas.
"""
import itertools


def to_index(x, y, w, h):
    """Converts a 2D coordinate to an linear index constrained to the canvas
    bounds.

    If a negative coordinate is provided"""
    invert  = lambda i, dim: dim + i if i < 0 else i
    lbound = lambda i, dim: 0 if i < 0 else i
    rbound = lambda i, dim: i if i < dim else dim - 1

    _x = reduce(lambda x, fn: fn(x, w), [invert, lbound, rbound], x)
    _y = reduce(lambda y, fn: fn(y, h), [invert, lbound, rbound], y)
    return _x + _y * w


def fill(x, y, f, w, h, drawing):
    "Fills an coordinate with given filler"
    i = to_index(x, y, w, h)
    return "%s%s%s" % (drawing[:i], f, drawing[i+1:])


def canvas(width, height, drawing):
    return " " * (width * height)


def line(x1, y1, x2, y2, w, h, drawing):
    "Draws a horizontal or vertical lines"
    dx, dy = range(x1, x2 + 1), range(y1, y2 + 1)

    if len(dx) > 1 and len(dy) > 1:
        raise ValueError

    return reduce(lambda d, xy: fill(*xy, f='x', w=w, h=h, drawing=d),
        itertools.product(dx, dy), drawing)


def rect(x1, y1, x2, y2, w, h, drawing):
    "Draws a rectangle"
    t = (x1, y1, x2, y1)
    r = (x2, y1, x2, y2)
    b = (x1, y2, x2, y2)
    l = (x1, y1, x1, y2)
    return reduce(lambda d, largs: line(*largs,
        w=w, h=h, drawing=d), (t,r,b,l), drawing)


def bucket(x, y, c, w, h, drawing):
    "Fills some area constrained to the canvas and/or lines"
    return fill(x, y, c, w, h, drawing)
