import unittest
from draw import canvas, line


BASE_CANVAS = " " * (20 * 4)


class CanvasTest(unittest.TestCase):

    def test_returns_a_2d_canvas(self):
        "Returns a canvas with given width and height"
        drawing = canvas(2, 2, None)
        self.assertEqual(drawing, "    ")

    def test_override_old_canvas(self):
        drawing = canvas(2, 2, "xxxxx")
        self.assertEqual(drawing, "    ")


@unittest.skip
class LineTest(unittest.TestCase):

    def test_horizontal_line(self):
        drawing = line(1, 2, 6, 2, BASE_CANVAS)
        self.assertEqual(canvas, """
        +--------------------+
        |                    |
        |xxxxxx              |
        |                    |
        |                    |
        +--------------------+
        """)

    def test_vertical_line(self):
        drawing = line(6, 3, 6, 4, BASE_CANVAS)

    def test_diagonal_line(self):
        pass



class RectTest(unittest.TestCase):
    pass


class FillTest(unittest.TestCase):
    pass
