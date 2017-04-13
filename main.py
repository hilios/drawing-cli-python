"""Main CLI application.
"""
import logging
import sys
from drawing import cmdparse, render


def run(canvas=None):
    "Recursively applies a command to the drawing"
    cmd = cmdparse.parse(raw_input("enter command: "))
    run(render(cmd, canvas))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', '-d', action='store_true')
    args = parser.parse_args()

    logging.basicConfig(format='%(levelname)s: %(message)s',
        level=logging.DEBUG if args.debug else logging.WARNING)

    try:
        run()
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)
