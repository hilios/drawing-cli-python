import unittest
import textwrap
from drawing.utils import pretty_render
from drawing.draw import canvas, fill, line, rect, bucket


W, H,  = (20, 4)
BASE_CANVAS = " " * (W * H)


class CanvasTest(unittest.TestCase):

    def test_returns_a_2d_canvas(self):
        "Returns a canvas with given width and height"
        drawing = canvas(2, 2, None)
        self.assertEqual(drawing, "    ")

    def test_override_old_canvas(self):
        drawing = canvas(2, 2, "xxxxx")
        self.assertEqual(drawing, "    ")


class FillerTest(unittest.TestCase):

    w, h = 3, 3
    canvas = " " * (w * h)

    def test_fill_coordinate(self):
        drawing = fill(1, 1, '*', self.w, self.h, self.canvas)
        self.assertEqual(drawing, "    *    ")

    def test_out_of_bounds(self):
        drawing = fill(11, 11, '*', self.w, self.h, self.canvas)
        self.assertEqual(drawing, "        *")

    def test_negative_index(self):
        drawing = fill(-1, -1, '*', self.w, self.h, self.canvas)
        self.assertEqual(drawing, "        *")

    def test_negative_out_of_bounds(self):
        drawing = fill(-11, -11, '*', self.w, self.h, self.canvas)
        self.assertEqual(drawing, "*        ")


class LineTest(unittest.TestCase):

    def test_horizontal_line(self):
        drawing = line(0, 1, 5, 1, W, H, BASE_CANVAS)
        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |                    |
        |xxxxxx              |
        |                    |
        |                    |
        +--------------------+
        """))

    def test_vertical_line(self):
        drawing = line(5, 2, 5, 3, W, H, BASE_CANVAS)
        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |                    |
        |                    |
        |     x              |
        |     x              |
        +--------------------+
        """))

    def test_diagonal_line(self):
        with self.assertRaises(ValueError):
            line(1, 2, 6, 4, W, H, BASE_CANVAS)


class RectTest(unittest.TestCase):

    def test_draw_rect(self):
        drawing = rect(15, 0, 19, 2, W, H, BASE_CANVAS)
        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |               xxxxx|
        |               x   x|
        |               xxxxx|
        |                    |
        +--------------------+
        """))


class BucketTest(unittest.TestCase):

    def base_drawing(self, *args):
        l1 = lambda c: line(0, 1, 5, 1, W, H, c)
        l2 = lambda c: line(5, 2, 5, 3, W, H, c)
        rc = lambda c: rect(15, 0, 19, 2, W, H, c)
        return reduce(lambda d, fn: fn(d), (l1,l2,rc) + args, BASE_CANVAS)

    def test_filling_the_canvas(self):
        bf = lambda c: bucket(9, 2, 'o', W, H, c)
        drawing = self.base_drawing(bf)

        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |oooooooooooooooxxxxx|
        |xxxxxxooooooooox   x|
        |     xoooooooooxxxxx|
        |     xoooooooooooooo|
        +--------------------+
        """))

    def test_fill_canvas_from_other_point(self):
        bf = lambda c: bucket(0, 0, '.', W, H, c)
        drawing = self.base_drawing(bf)

        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |...............xxxxx|
        |xxxxxx.........x   x|
        |     x.........xxxxx|
        |     x..............|
        +--------------------+
        """))

        def test_fill_just_the_squares(self):
            bf = lambda c: bucket(0, 0, '*', W, H, c)
            br = lambda c: bucket(17, 1, '@', W, H, c)
            drawing = self.base_drawing(bf, br)

            self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
            +--------------------+
            |               xxxxx|
            |xxxxxx         x@@@x|
            |*****x         xxxxx|
            |*****x              |
            +--------------------+
            """))
