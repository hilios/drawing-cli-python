"""The command parser utilities
"""
import copy
import logging
import re


CMD_PARSER = re.compile("[A-Z]{1}(\s(\d+|[a-z]{1})){0,4}$")


def parse(cmd):
    "Parses a command input"
    if CMD_PARSER.match(cmd):
        return tuple(cmd.split())
    else:
        logging.warn("Invalid input")
        return (None,)


def handle(*constraints, **kwargs):
    """Adapt some given function to a command input applying a pattern matching
    constraints."""
    handlename, types = constraints[0], constraints[1:]
    def action_decorator(fn):
        def wrapper(cmd, canvas):
            cmdname, params = cmd[0], cmd[1:]

            if cmdname is not handlename:
                return canvas

            if kwargs.get('require_canvas', True) and canvas is None:
                logging.warn('Please, create a canvas before drawing')
                return canvas

            try:
                if len(params) is not len(types):
                    raise ValueError

                args = tuple([fmt(param) for (param, fmt) in zip(params, types)])
                logging.debug("Executing %s with params: %s" % (cmdname, args))
                return fn(*args, canvas=canvas)

            except ValueError:
                logging.warn("Wrong input")
                return canvas

        return wrapper

    return action_decorator
