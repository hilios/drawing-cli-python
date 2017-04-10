"""Discovers and runs all unit tests.
"""
import os

if __name__ == '__main__':
    import unittest
    suite = unittest.defaultTestLoader.discover('.', pattern="*_test.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
