"""
This file contains the TestHtmlSanitizer class which contains 
multiple different test used to test the html parser
"""

import sys
import json
import difflib
import unittest

sys.path.append('..')
from html_sanitizer import HtmlSanitizer


class TestHtmlSanitizer(unittest.TestCase):
    """
    This class is used to test the html parser class
    """

    # TODO

# Do not run on imports
if __name__ == '__main__':
    unittest.main()
