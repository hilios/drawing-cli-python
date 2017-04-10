"""The command parser utilities
"""
import copy
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


def handle(*constraints, **kwargs):
    """Adapt some given function to a command input, constrained by the arguments."""
    action_constraint = constraints[0]
    types = constraints[1:]

    def action_decorator(fn):
        def wrapper(cmd, drawing):
            action, params = (cmd[0], cmd[1:])

            if action is not action_constraint:
                return drawing

            if kwargs.get('require_canvas', True) and drawing is None:
                logging.warn('Please, create a canvas before drawing')
                return drawing

            try:
                if len(params) is not len(types):
                    raise ValueError

                args = tuple([fmt(param) for (param, fmt) in zip(params, types)])
                logging.debug("Executing %s with params: %s" % (action, args))
                return fn(*args, drawing=drawing)

            except ValueError:
                logging.warn("Wrong input")
                return drawing

        return wrapper

    return action_decorator
