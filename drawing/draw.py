"""Draw stuff in the canvas in a purely functional style, assuring imutability.

All X and Y coordinates are zero-based positions relative to the canvas.
"""
import itertools


def index(x, y, w, h):
    """Converts a 2D coordinate to an linear index constrained to the canvas
    bounds"""
    lbound = lambda i, dim: 0 if i < 0 else i
    rbound = lambda i, dim: i if i < dim else dim - 1

    _x = reduce(lambda x, fn: fn(x, w), [lbound, rbound], x)
    _y = reduce(lambda y, fn: fn(y, h), [lbound, rbound], y)
    return _x + _y * w


def fill(x, y, f, w, h, drawing):
    "Fills an coordinate with given filler"
    i = index(x, y, w, h)
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
    """Fills some area constrained to the canvas and/or lines using a flood-fill
    algorithm"""
    i = index(x, y, w, h)
    if drawing[i] is " ":
        t = (x, y - 1)
        r = (x + 1, y)
        b = (x, y + 1)
        l = (x - 1, y)
        ixs = [(m,n) for m,n in (t,r,b,l) if m >= 0 and m < w and n >= 0 and n < h]

        return reduce(lambda d, xy: bucket(*xy, c=c, w=w, h=h, drawing=d), ixs,
            fill(x, y, c, w, h, drawing))
    else:
        return drawing
