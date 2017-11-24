"""
This file contains the TestMarkdownSanitizer class which contains 
multiple different test used to test the markdown parser
"""

import sys
import json
import difflib
import unittest

sys.path.append('..')
from markdown_sanitizer import MarkdownSanitizer


class TestMarkdownSanitizer(unittest.TestCase):
    """
    This class is used to test the markdown parser class
    """

    # TODO

# Do not run on imports
if __name__ == '__main__':
    unittest.main()
