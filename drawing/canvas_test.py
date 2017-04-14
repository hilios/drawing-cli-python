import unittest
import textwrap
from drawing.canvas import Canvas, blank_canvas


class CavasTest(unittest.TestCase):
    def assertCanvas(self, canvas, expected_canvas):
        self.assertEqual(canvas.drawing, expected_canvas.drawing)

    def assertRender(self, canvas, expected_render):
        self.assertEqual(canvas.render(), textwrap.dedent(expected_render))

    def test_returns_a_new_blank_canvas(self):
        canvas = blank_canvas(2, 2)
        self.assertCanvas(canvas, Canvas(2, 2, "    "))

    def test_creating_a_new_canvas(self):
        canvas = Canvas(3, 3, "xxxxxxxxx")
        self.assertEqual(canvas.w, 3)
        self.assertEqual(canvas.h, 3)
        self.assertEqual(canvas.drawing, "xxxxxxxxx")

    def test_render(self):
        canvas = blank_canvas(20, 4)
        self.assertRender(canvas, """
        +--------------------+
        |                    |
        |                    |
        |                    |
        |                    |
        +--------------------+
        """)

    def test_fill_coordinate(self):
        canvas = blank_canvas(3, 3).fill(1, 1, '*')
        self.assertEqual(canvas.drawing, "    *    ")

    def test_fill_out_of_bounds(self):
        canvas = blank_canvas(3, 3).fill(11, 11, '*')
        self.assertEqual(canvas.drawing, "        *")

    def test_fill_negative_index(self):
        canvas = blank_canvas(3, 3).fill(-1, -1, '*')
        self.assertEqual(canvas.drawing, "*        ")

    def test_horizontal_line(self):
        canvas = blank_canvas(20, 4).line(0, 1, 5, 1)
        self.assertRender(canvas, """
        +--------------------+
        |                    |
        |xxxxxx              |
        |                    |
        |                    |
        +--------------------+
        """)

    def test_vertical_line(self):
        canvas = blank_canvas(20, 4).line(5, 2, 5, 3)
        self.assertRender(canvas, """
        +--------------------+
        |                    |
        |                    |
        |     x              |
        |     x              |
        +--------------------+
        """)

    def test_diagonal_line(self):
        with self.assertRaises(ValueError):
            blank_canvas(20, 4).line(1, 2, 6, 4)

    def test_draw_rect(self):
        canvas = blank_canvas(20, 4).rect(15, 0, 19, 2)
        self.assertRender(canvas, """
        +--------------------+
        |               xxxxx|
        |               x   x|
        |               xxxxx|
        |                    |
        +--------------------+
        """)

    def test_filling_the_canvas(self):
        canvas = blank_canvas(20, 4)\
            .line(0, 1, 5, 1)\
            .line(5, 2, 5, 3)\
            .rect(15, 0, 19, 2)\
            .bucket(9, 2, 'o')

        self.assertRender(canvas, """
        +--------------------+
        |oooooooooooooooxxxxx|
        |xxxxxxooooooooox   x|
        |     xoooooooooxxxxx|
        |     xoooooooooooooo|
        +--------------------+
        """)

    def test_fill_canvas_from_other_point(self):
        canvas = blank_canvas(20, 4)\
        .line(0, 1, 5, 1)\
        .line(5, 2, 5, 3)\
        .rect(15, 0, 19, 2)\
        .bucket(0, 0, '.')

        self.assertRender(canvas, """
        +--------------------+
        |...............xxxxx|
        |xxxxxx.........x   x|
        |     x.........xxxxx|
        |     x..............|
        +--------------------+
        """)

    def test_fill_just_the_squares(self):
        canvas = blank_canvas(20, 4)\
            .line(0, 1, 5, 1)\
            .line(5, 2, 5, 3)\
            .rect(15, 0, 19, 2)\
            .bucket(0, 2, '*')\
            .bucket(17, 1, '@')

        self.assertRender(canvas, """
        +--------------------+
        |               xxxxx|
        |xxxxxx         x@@@x|
        |*****x         xxxxx|
        |*****x              |
        +--------------------+
        """)
