import unittest
import textwrap
from drawing.utils import pretty_render


class PrettyRenderTest(unittest.TestCase):

    def test_should_return_a_bordered_canvas(self):
        canvas = pretty_render(20, 4, " " * 80)
        self.assertEqual(canvas, textwrap.dedent("""
        +--------------------+
        |                    |
        |                    |
        |                    |
        |                    |
        +--------------------+
        """))

    
