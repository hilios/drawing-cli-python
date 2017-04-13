"""Discovers and runs all unit tests.
"""
import logging
import sys
import unittest


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR,
        format='%(asctime)s\t%(levelname)-8s\t%(message)s')

    suite = unittest.defaultTestLoader.discover('.', pattern="*_test.py")
    unittest.TextTestRunner(stream=sys.stdout, verbosity=1).run(suite)
