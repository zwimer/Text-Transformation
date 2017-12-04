"""
This file contains the TestSystemIntegration class which contains test
cases for the full integrated text transformation system.

Currently, tests that fail due to the same error as another test (most of the
html tests) have been prepended with donotrun_ and only the original test with
that error has been left runnable
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

# ============================================================================
# PLAINTEXT
# ============================================================================

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

# ============================================================================
# HTML
# ============================================================================

    def donotrun_test_html_abbreviated_tags(self):
        """
        throws AssertionError: If test case fails
        System test for abbreviated tags HTML test plan
        """
        input_fname = "../../test-plans/HTML/Abbreviated-tags/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Abbreviated-tags/output.txt"
        actual_output_fname = "../../test-plans/HTML/Abbreviated-tags/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def donotrun_test_html_duplicate_metadata(self):
        """
        throws AssertionError: If test case fails
        System test for duplicate metadata HTML test plan
        """
        input_fname = "../../test-plans/HTML/Duplicate-meta-data/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Duplicate-meta-data/output.txt"
        actual_output_fname = "../../test-plans/HTML/Duplicate-meta-data/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def donotrun_test_html_duplicate_title(self):
        """
        throws AssertionError: If test case fails
        System test for duplicate title HTML test plan
        """
        input_fname = "../../test-plans/HTML/Duplicate-title/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Duplicate-title/output.txt"
        actual_output_fname = "../../test-plans/HTML/Duplicate-title/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

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

    def test_html_html_in_javascript_comments(self):
        """
        throws AssertionError: If test case fails
        System test for html in javascript comments HTML test plan
        """
        input_fname = "../../test-plans/HTML/Html-in-javascript-comments/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Html-in-javascript-comments/output.txt"
        actual_output_fname = "../../test-plans/HTML/Html-in-javascript-comments/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def donotrun_test_html_inline_css(self):
        """
        throws AssertionError: If test case fails
        System test for inline css HTML test plan
        """
        input_fname = "../../test-plans/HTML/Inline-CSS/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Inline-CSS/output.txt"
        actual_output_fname = "../../test-plans/HTML/Inline-CSS/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def donotrun_test_html_inline_php(self):
        """
        throws AssertionError: If test case fails
        System test for inline php HTML test plan
        """
        input_fname = "../../test-plans/HTML/Inline-PHP/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Inline-PHP/output.txt"
        actual_output_fname = "../../test-plans/HTML/Inline-PHP/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def donotrun_test_html_Internal_css(self):
        """
        throws AssertionError: If test case fails
        System test for internal css HTML test plan
        """
        input_fname = "../../test-plans/HTML/Internal-CSS/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Internal-CSS/output.txt"
        actual_output_fname = "../../test-plans/HTML/Internal-CSS/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def test_html_plain_text(self):
        """
        throws AssertionError: If test case fails
        System test for plain-text HTML test plan
        """
        input_fname = "../../test-plans/HTML/Plain-text/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Plain-text/output.txt"
        actual_output_fname = "../../test-plans/HTML/Plain-text/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def donotrun_test_html_script_tags(self):
        """
        throws AssertionError: If test case fails
        System test for script tags HTML test plan
        """
        input_fname = "../../test-plans/HTML/Script-Tags/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Script-Tags/output.txt"
        actual_output_fname = "../../test-plans/HTML/Script-Tags/actual.txt"

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

    def test_md_inline_image(self):
        """
        throws AssertionError: If test case fails
        System test for inline image md test plan
        """
        input_fname = "../../test-plans/Markdown/Inline-Image/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Inline-Image/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Inline-Image/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)

    def test_md_inline_link_style(self):
        """
        throws AssertionError: If test case fails
        System test for inline link style md test plan
        """
        input_fname = "../../test-plans/Markdown/Inline-Link-Style/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Inline-Link-Style/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Inline-Link-Style/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
            expected_output_fname, actual_output_fname)


if __name__ == "__main__":
    unittest.main()
