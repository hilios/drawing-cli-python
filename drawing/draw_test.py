import unittest
import textwrap
from drawing.utils import pretty_render
from drawing.draw import canvas, point, line, rect, fill


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


class PosAndPointTest(unittest.TestCase):

    w, h = 3, 3
    canvas = " " * (w * h)

    def test_draw_point(self):
        drawing = point(1, 1, '*', self.w, self.h, self.canvas)
        self.assertEqual(drawing, "    *    ")

    def test_out_of_bounds(self):
        drawing = point(10, 10, '*', 3, 3, " " * 3**2)
        self.assertEqual(drawing, "         *")


class LineTest(unittest.TestCase):

    def test_horizontal_line(self):
        drawing = line(1, 2, 6, 2, W, H, BASE_CANVAS)
        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |                    |
        |xxxxxx              |
        |                    |
        |                    |
        +--------------------+
        """))

    def test_vertical_line(self):
        drawing = line(6, 3, 6, 4, W, H, BASE_CANVAS)
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
        drawing = rect(16, 1, 20, 3, W, H, BASE_CANVAS)
        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |               xxxxx|
        |               x   x|
        |               xxxxx|
        |                    |
        +--------------------+
        """))


class FillTest(unittest.TestCase):

    def test_filling_a_rect(self):
        l1 = lambda c: line(1, 2, 6, 2, W, H, c)
        l2 = lambda c: line(6, 3, 6, 4, W, H, c)
        rc = lambda c: rect(16, 1, 20, 3, W, H, c)

        drawing = reduce(lambda d, fn: fn(d), (l1,l2,rc), BASE_CANVAS)

        self.assertEqual(pretty_render(W, H, drawing), textwrap.dedent("""
        +--------------------+
        |               xxxxx|
        |xxxxxx         x   x|
        |     x         xxxxx|
        |     x              |
        +--------------------+
        """))

        fl = lambda c: fill(10, 3, 'o', c)

        print pretty_render(W, H, drawing)
