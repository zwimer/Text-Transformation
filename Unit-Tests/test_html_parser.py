"""
This file contains the TestHtmlParser class which contains 
multiple different test used to test the html parser
"""

import sys
import json
import difflib
import unittest

sys.path.append('..')
from Bs4Wrapper import Bs4Wrapper

class TestHtmlParser(unittest.TestCase):
    """
    This class is used to test the html parser class
    """

    def run_test_check_output(self, input_data, expected_output):
        """
        :param input_data: The data to be input to the parser
        :param expected_output: The expected output of the parser
        :throws AssertionError: if test fails
        :returns: nothing
        """
        
        # Create the new parser
        parser = Bs4Wrapper(input_data)

        # Extract the plain text lists
        output = parser.extract_plain_text_lists()

        # Standardize method of converting text to json
        def to_json(text): return json.dumps(output, indent=4, separators=(',', ':'))

        # Convert the output and expected output to json forms
        expected_output_json = to_json(expected_output)
        output_json = to_json(output)

        # Diff the results for the user
        self.diff(expected_output_json, output_json)

        # Assert equality
        self.assertEquals(expected_output_json, output_json)

    @staticmethod
    def diff(expected_output, output):
        """
        :param expected_output: The expected output
        :param output: The actual output
        Diff the expected and actual output for the user
        """

        # If the strings are the same, just return
        if expected_output == output:
            return
        
        # Create the diff
        diff = difflib.ndiff( expected_output.split('\n'), output.split('\n') )

        # Print the diff
        print(''.join(diff))

    def test_general_1(self):
        """
        :throws AssertionError: If test cases fail
        :returns: nothing
        """

        # Test Input
        html = '''<title> My Amazing book </title>
                  <meta name="author" content="Meg">
                  Hello World book'''
    
        # Expected title
        title = 'My amazing book'

        # Expected metadata
        metadata = { 
            'author' : 'Meg'
        }

        # Expected output
        expected_output = [
            [ 'My', 'Amazing', 'book' ],
            [ 'Hello', 'World', 'book' ]
        ];

        # Test the output
        self.run_test_check_output(html, expected_output)

# Do not run on imports
if __name__ == '__main__':
    unittest.main()
