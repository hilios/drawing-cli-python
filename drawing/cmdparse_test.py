import unittest
from drawing.cmdparse import action, parse


@action('A', fmts=(int, str,), require_canvas=True)
def test_cmd(cmd, drawing):
    return cmd + (drawing,)


@action('B', require_canvas=False)
def test_cmd_wo_canvas(cmd, drawing):
    return cmd + (drawing,)


class ActionTest(unittest.TestCase):

    def test_action_w_fmt_and_require_canvas(self):
        "If canvas provided return the function or returns the drawing otherwise"
        self.assertEqual(test_cmd(('A', '1', 'c'), "  "), (1, 'c', "  "))
        self.assertEqual(test_cmd(('A', '1', 'c'), None), None)

    def test_action_wo_fmt_or_require_canvas(self):
        "Always return the function no matter what"
        self.assertEqual(test_cmd_wo_canvas(('B',), "  "), ("  ",))
        self.assertEqual(test_cmd_wo_canvas(('B',), None), (None,))

    def test_fmt_incorrect_args(self):
        "If params not match the formatters return the drawing"
        self.assertEqual(test_cmd(('A', '1', 'c', '2'), "  "), "  ")
        self.assertEqual(test_cmd(('A', '1',), "  "), "  ")

    def test_fmt_value_error(self):
        "If fmt could not be applied return the drawing"
        self.assertEqual(test_cmd(('A', 'c', '1'), "  "), "  ")
        self.assertEqual(test_cmd(('A', 'c', '1'), None), None)



class ParseTest(unittest.TestCase):

    def test_correct_matches(self):
        self.assertEqual(parse("C 20 4"), ("C", "20", "4",))
        self.assertEqual(parse("L 1 2 3 4"), ("L", "1", "2", "3", "4",))
        self.assertEqual(parse("R 1 2 3 4"), ("R", "1", "2", "3", "4",))
        self.assertEqual(parse("B 1 2 c"), ("B", "1", "2", "c"))
        self.assertEqual(parse("Q"), ("Q",))

    def test_incorrect_matches(self):
        self.assertEqual(parse("B 1 ccc"), (None,))
        self.assertEqual(parse("CC 20 30"), (None,))
        self.assertEqual(parse("q"), (None,))
        self.assertEqual(parse("Lorem ipsum dolor"), (None,))
