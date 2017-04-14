import textwrap
import itertools


BLANK_CHAR = " "
LINE_CHAR = "x"


class Canvas:
    "An objects that allow drawing in it"
    def __init__(self, width, height, drawing):
        self.w = width
        self.h = height
        self.drawing = drawing

    def render(self):
        "Renders a beautifull canvas with borders"
        border = "-" * self.w
        lines  = ["|%s|" % self.drawing[(i * self.w):(i * self.w + self.w)] for i in range(self.h)]

        return textwrap.dedent("""
        +{border}+
        {drawing}
        +{border}+
        """).format(border=border, drawing="\n".join(lines))

    def index(self, x, y):
        "Converts a 2D coordinate to an linear index constrained to the canvas bounds"
        lbound = lambda i, dim: 0 if i < 0 else i
        rbound = lambda i, dim: i if i < dim else dim - 1

        _x = reduce(lambda x, fn: fn(x, self.w), [lbound, rbound], x)
        _y = reduce(lambda y, fn: fn(y, self.h), [lbound, rbound], y)
        return _x + _y * self.w

    def fill(self, x, y, filler):
        "Fills an coordinate with given filler"
        i = self.index(x, y)
        return Canvas(self.w, self.h, "%s%s%s" % (self.drawing[:i], filler, self.drawing[i+1:]))

    def line(self, x1, y1, x2, y2):
        "Draws a horizontal or vertical lines"
        xs = range(x1, x2 + 1) if (x1 < x2) else range(x2, x1 + 1)
        ys = range(y1, y2 + 1) if (y1 < y2) else range(y2, y1 + 1)

        if len(xs) > 1 and len(ys) > 1:
            raise ValueError

        return reduce(lambda c, xy: c.fill(*xy, filler=LINE_CHAR), itertools.product(xs, ys), self)

    def rect(self, x1, y1, x2, y2):
        "Draws a rectangle"
        t = (x1, y1, x2, y1)
        r = (x2, y1, x2, y2)
        b = (x1, y2, x2, y2)
        l = (x1, y1, x1, y2)
        return reduce(lambda c, largs: c.line(*largs), (t,r,b,l), self)

    def bucket(self, x, y, color):
        "Fills some area constrained to the canvas and/or lines using a flood-fill algorithm"
        i = self.index(x, y)
        if self.drawing[i] is BLANK_CHAR:
            t = (x, y - 1)
            r = (x + 1, y)
            b = (x, y + 1)
            l = (x - 1, y)
            adj = [(m,n) for m,n in (t,r,b,l) if m >= 0 and m < self.w and n >= 0 and n < self.h]

            return reduce(lambda c, xy: c.bucket(*xy, color=color), adj, self.fill(x, y, color))
        else:
            return self


def blank_canvas(width, height):
    return Canvas(width, height, BLANK_CHAR * (width * height))
