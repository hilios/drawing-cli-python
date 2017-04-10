"""The command parser utilities
"""
import logging
import re


CMD_PARSER = re.compile("^(%s)$" % "|".join("""
(C) (\d+) (\d+)
(L) (\d+) (\d+) (\d+) (\d+)
(R) (\d+) (\d+) (\d+) (\d+)
(B) (\d+) (\d+) (\w)
(Q)
""".split("\n")))


def action(action, require_canvas=True):
    "Defines an action constraint."
    def action_decorator(fn):
        def wrapper(cmd, drawing):
            if cmd[0] is not action:
                return drawing

            if require_canvas and drawing is None:
                logging.warn('Please, create a canvas before drawing')
                return drawing

            logging.info("Executing command: %s" % " ".join(cmd))
            return fn(cmd, drawing)

        return wrapper

    return action_decorator


def parse(cmd):
    "Given an cmd input "
    parser = CMD_PARSER.match(cmd)
    if parser:
        cmd_group = parser.groups()
        return tuple([val for val in cmd_group[1:] if val != None])
    else:
        logging.warn("Invalid input")
        return (None,)
