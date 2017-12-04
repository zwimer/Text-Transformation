"""
This file contains the TestSystemIntegration class which contains test
cases for the full integrated text transformation system.
"""

import sys
import json
import difflib
import unittest

sys.path.append('..')
import text_transformation


class TestSystemIntegration(unittest.TestCase):
    """
    This class tests text transformation system
    """

    def assert_equality(self, expected_fname, actual_fname):
        """
        param expected_fname: filename of the expected output
        param actual_fname: filename of the actual output
        throws AssertionError: if the values are not equal
        Loads the json contents of each file and assert that actual == expected
        Print them out and throw an assertion error if they differ
        """

        expected_f = open(expected_fname, 'r')
        expected = json.load( expected_f )
        expected_f.close()

        actual_f = open(actual_fname, 'r')
        actual = json.load( actual_f )
        actual_f.close()

        # Assert that the types match
        self.assertEqual(type(expected), type(actual))

        self.maxDiff = None
        # Try to assert equality
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            raise

    def run_test_check_output(self, input_fname, input_type,
      expected_output_fname, actual_output_fname):
        """
        param input_fname: filename of the json input file
        param input_type: file type of input
        param expected_output_fname: filename of the json expected output file
        param actual_output_fname: name for the output file
        throws AssertionError: if test fails
        Test that the output matches the expected
        """
        text_transformation.main( (input_fname, input_type), actual_output_fname)
        self.assert_equality(expected_output_fname, actual_output_fname)

    # TESTS

    # Plaintext tests
    def test_casing(self):
        """
        throws AssertionError: If test case fails
        System test for casing
        """
        input_fname = "../../test-plans/Casing/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Casing/output.txt"
        actual_output_fname = "../../test-plans/Casing/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def test_punctuation(self):
        """
        throws AssertionError: If test case fails
        System test for punctuation
        """
        input_fname = "../../test-plans/Punctuation/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Punctuation/output.txt"
        actual_output_fname = "../../test-plans/Punctuation/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def test_stop_punctuation(self):
        """
        throws AssertionError: If test case fails
        System test for stop punctuation
        """
        input_fname = "../../test-plans/Stop-Punctuation/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Stop-Punctuation/output.txt"
        actual_output_fname = "../../test-plans/Stop-Punctuation/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def test_stop_words(self):
        """
        throws AssertionError: If test case fails
        System test for stopwords
        """
        input_fname = "../../test-plans/Stop-Words/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Stop-Words/output.txt"
        actual_output_fname = "../../test-plans/Stop-Words/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def test_whitespace(self):
        """
        throws AssertionError: If test case fails
        System test for stopwords
        """
        input_fname = "../../test-plans/Whitespace/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Whitespace/output.txt"
        actual_output_fname = "../../test-plans/Whitespace/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    # HTML tests - sticking only to general ones for now
    def test_html_general_1(self):
        """
        throws AssertionError: If test case fails
        System test for general-1 HTML test plan
        """
        input_fname = "../../test-plans/HTML/General-1/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/General-1/output.txt"
        actual_output_fname = "../../test-plans/HTML/General-1/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def test_html_general_2(self):
        """
        throws AssertionError: If test case fails
        System test for general-2 HTML test plan
        """
        input_fname = "../../test-plans/HTML/General-2/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/General-2/output.txt"
        actual_output_fname = "../../test-plans/HTML/General-2/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    # Markdown tests
    # Just general tests at first
    def test_md_general_1(self):
        """
        throws AssertionError: If test case fails
        System test for general-1 md test plan
        """
        input_fname = "../../test-plans/Markdown/General-1/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/General-1/output.txt"
        actual_output_fname = "../../test-plans/Markdown/General-1/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

if __name__ == "__main__":
    unittest.main()
