"""The command parser utilities
"""
import logging
import re


CMD_PARSER = re.compile("[A-Z]{1}(\s(\d+|[a-z]{1}))*$")


def parse(cmd):
    "Parses a command input"
    if CMD_PARSER.match(cmd):
        return tuple(cmd.split())
    else:
        logging.warn("Invalid input")
        return (None,)


def action(expected_action, fmts=tuple(), require_canvas=True):
    "Defines an action constraint and format"
    def action_decorator(fn):
        def wrapper(cmd, drawing):
            action, params = (cmd[0], cmd[1:])

            if action is not expected_action:
                return drawing

            if require_canvas and drawing is None:
                logging.warn('Please, create a canvas before drawing')
                return drawing

            try:
                if len(params) is not len(fmts):
                    raise ValueError

                fmtp = tuple([fmt(param) for (param, fmt) in zip(params, fmts)])
                logging.debug("Executing %s with params: %s" % (action, fmtp))
                return fn(fmtp, drawing)

            except ValueError:
                logging.warn("Wrong input")
                return drawing

        return wrapper

    return action_decorator
