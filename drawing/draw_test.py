import unittest
from draw import canvas


class CanvasTest(unittest.TestCase):

    def test_returns_a_2d_canvas(self):
        "Returns a canvas with given width and height"
        self.assertEqual(canvas(1, 1, None), " ")

    def test_override_old_canvas(self):
        self.assertEqual(canvas(1, 1, "xxxxx"), " ")


class LineTest(unittest.TestCase):
    pass


class RectTest(unittest.TestCase):
    pass


class FillTest(unittest.TestCase):
    pass
