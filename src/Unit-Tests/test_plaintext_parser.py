"""
This file contains the TestPlaintextSanitizer class which contains
multiple different test used to test the plaintext parser
"""

import sys
import json
import difflib
import unittest

sys.path.append('..')
from text_sanitizer import TextSanitizer

class TestPlaintextSanitizer(unittest.TestCase):
    """
    This class is used to test the markdown parser class
    """

    def assert_equality(self, expected, actual):
        """
        :param expected: The expected value
        :param actual: The actual value
        :throws AssertionError: if the values are not equal
        :returns: nothing
        Assert that actual == expected. Print them out
        and throw an assertion error if they differ
        """

        # Assert that the types match
        self.assertEqual(type(expected), type(actual))

        # If the types are jsons, make them strings
        if type(actual) is [ list, dict ]:
            expected = json_to_str(expected)

        # Test to ensure equality
        try:
            self.assertEqual(actual, expected)

        # If the assertion fails
        except AssertionError:
            print('*** Assertion failed! ***')
            print('Actual:' + str(actual))
            print('Expected:' + str(expected))
            print('*** Re-emitting error ***')
            raise

    def run_test_check_output(self, input_data, expected_output):
        """
        :param input_data: The data to be input to the parser
        :param expected_output: The expected output of the parser
        :throws AssertionError: if test fails
        :returns: nothing
        Test that the extracted output matches the expected
        """
        parser = TextSanitizer(input_data)
        output = parser.sanitize()

        self.assert_equality(expected_output, output)

    def test_casing(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser lower cases all characters
        """

        # Test input and all expected outputs
        pt = ('HeLLo WoRLd I hAvE a CaSiNg PrObLeM')
        output = [['hello', 'world', 'i', 'have', 'a', 'casing', 'problem']]
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(pt, output)

    def test_punctuation(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes punctuation
        """

        # Test input and all expected outputs
        pt = ('This. Sentence; ; Has! Punctuation&!!* ,Wow')
        output = [['this', 'sentence', 'has', 'punctuation', 'wow']]
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(pt, output)

    def test_stop_punctuation(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser properly splits clauses via stop punctuation
        """

        # Test input and all expected outputs
        pt = ('The string\n>is a stop word')
        output = [['the', 'string'], ['is', 'a', 'stop', 'word']]
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(pt, output)

    def test_whitespace(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes all extraneous whitespace
        """

        # Test input and all expected outputs
        pt = ('This\tis line\t\tone!\n\n\nHere we\t have line two\t!\n')
        output = [['this', 'is', 'line', 'one'],
                  ['here', 'we', 'have', 'line', 'two']]
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(pt, output)
        
# Do not run on imports
if __name__ == '__main__':
    unittest.main()
