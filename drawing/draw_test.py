import unittest
import textwrap
from drawing.utils import pretty_render
from drawing.draw import canvas, line, rect


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


@unittest.skip
class FillTest(unittest.TestCase):
    pass
