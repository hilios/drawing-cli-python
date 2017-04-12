"""Draw stuff
"""
import itertools


def pos(x, y, w, h):
    _x = abs(x) if x < w else w
    _y = abs(y) if y < h else h
    return _x + _y * w


def point(x, y, filler, w, h, drawing):
    i = pos(x, y, w, h)
    return "%s%s%s" % (drawing[:i], filler, drawing[i+1:])


def canvas(width, height, drawing):
    return " " * (width * height)


def line(x1, y1, x2, y2, w, h, drawing):
    dx, dy = range(x1 - 1, x2), range(y1 - 1, y2)

    if len(dx) > 1 and len(dy) > 1:
        raise ValueError

    return reduce(lambda d, xy: point(*xy, filler='x', w=w, h=h, drawing=d),
        itertools.product(dx, dy), drawing)


def rect(x1, y1, x2, y2, w, h, drawing):
    t = (x1, y1, x2, y1)
    r = (x2, y1, x2, y2)
    b = (x1, y2, x2, y2)
    l = (x1, y1, x1, y2)

    return reduce(lambda d, largs: line(*largs,
        w=w, h=h, drawing=d), (t,r,b,l), drawing)


def fill(x, y, color, drawing):
    raise NotImplementedError
