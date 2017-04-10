"""Discovers and runs all unit tests.
"""
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s\t%(levelname)-8s\t%(message)s')

    import unittest
    suite = unittest.defaultTestLoader.discover('.', pattern="*_test.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
