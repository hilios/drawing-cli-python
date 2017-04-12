"""Discovers and runs all unit tests.
"""
import logging
import sys


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR,
        format='%(asctime)s\t%(levelname)-8s\t%(message)s')

    import unittest
    suite = unittest.defaultTestLoader.discover('.', pattern="*_test.py")
    unittest.TextTestRunner(stream=sys.stdout, verbosity=1).run(suite)
