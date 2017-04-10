"""
"""
import logging
from drawing import cmdparse, draw


def run(drawing=None):
    "Recursively applies a command to the drawing"
    cmd = cmdparse.parse(raw_input("enter command: "))
    run(draw(cmd, drawing))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', '-d', action='store_true')
    args = parser.parse_args()

    logging.basicConfig(format='> %(message)s',
        level=logging.DEBUG if args.debug else logging.WARNING)

    try:
        run()
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)
