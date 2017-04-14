"""Utilities functions.
"""
import textwrap
import sys


def pretty_render(width, height, drawing):
    "Renders a beautifull canvas with borders"
    border = "-" * width
    lines  = ["|%s|" % drawing[(i * width):(i * width + width)] for i in range(height)]

    return textwrap.dedent("""
    +{border}+
    {drawing}
    +{border}+
    """).format(border=border, drawing="\n".join(lines))
