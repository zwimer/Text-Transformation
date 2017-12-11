"""
This file contains the TestSystemIntegration class which contains test
cases for the full integrated text transformation system.

Currently, tests that fail due to the same error as another test (most of the
html tests) have been prepended with  and only the original test with
that error has been left runnable
"""

import sys
import os
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
        expected = json.load(expected_f)
        expected_f.close()

        actual_f = open(actual_fname, 'r')
        actual = json.load(actual_f)
        actual_f.close()

        # Assert that the types match
        self.assertEqual(type(expected), type(actual))

        self.maxDiff = None
        # Try to assert equality
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            raise

    def assert_file_does_not_exist(self, filepath):
        """
        param filepath: relative path to file to check
        throws AssertionError: if file exists
        Checks that the file specified does not exist
        """
        self.assertFalse(os.path.isfile(filepath))

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
        text_transformation.main(
            (input_fname, input_type), actual_output_fname)
        self.assert_equality(expected_output_fname, actual_output_fname)

    def run_test_no_output(self, input_fname, input_type, output_fname):
        """
        param input_fname: filename of the json input file
        param input_type: file type of input
        param output_fname: name for the output file
        throws AssertionError: if test fails)
        Test that the given input produces an error/ system exit and
        therefore no output
        """

        with self.assertRaises(SystemExit):
            text_transformation.main((input_fname, input_type), output_fname)

        self.assert_file_does_not_exist(output_fname)

# ============================================================================
# SYSTEM
# ============================================================================

    def test_improper_number_of_arguments(self):
        """
        throws AssertionError: If system does not exit and creates output
        System test for binary files (should be ignored)
        """
        output_fname = "../../test-plans/System/Empty/output.txt"

        # Specific test because specified arguemnts
        # Check for failure with one or three arguments
        with self.assertRaises(SystemExit):
            text_transformation.main((None,), output_fname)
            text_transformation.main((None, None, None), output_fname)

        self.assert_file_does_not_exist(output_fname)

    def test_file_type_not_allowed(self):
        """
        throws AssertionError: If system does not exit and creates output
        System test for file types that are not txt, html, md
        """
        input_fname = "../../test-plans/System/File-Type-Not-Allowed/input.php"
        input_type = "php"
        output_fname = "../../test-plans/System/File-Type-Not-Allowed/output.txt"

        self.run_test_no_output(input_fname, input_type, output_fname)

    def test_binary(self):
        """
        throws AssertionError: If system does not exit and creates output
        System test for binary files (should be ignored)
        """
        input_fname = "../../test-plans/System/Binary-File/input.jpg"
        input_type = "txt"  # So that file opening failure is tested instead of type checking
        output_fname = "../../test-plans/System/Binary-File/output.txt"

        # Specific test because of binary reading error
        with self.assertRaises(UnicodeDecodeError):
            text_transformation.main((input_fname, input_type), output_fname)

        self.assert_file_does_not_exist(output_fname)

    def test_empty_text_file(self):
        """
        throws AssertionError: If system does not exit and creates output
        System test for file types that are not txt, html, md
        """
        input_fname = "../../test-plans/System/Empty-Text-File/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/System/Empty-Text-File/output.txt"
        actual_output_fname = "../../test-plans/System/Empty-Text-File/actual.txt"

        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

# ============================================================================
# PLAINTEXT
# ============================================================================

    def test_casing(self):
        """
        throws AssertionError: If test case fails
        System test for casing
        """
        input_fname = "../../test-plans/Plaintext/Casing/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Plaintext/Casing/output.txt"
        actual_output_fname = "../../test-plans/Plaintext/Casing/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_punctuation(self):
        """
        throws AssertionError: If test case fails
        System test for punctuation
        """
        input_fname = "../../test-plans/Plaintext/Punctuation/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Plaintext/Punctuation/output.txt"
        actual_output_fname = "../../test-plans/Plaintext/Punctuation/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_stop_punctuation(self):
        """
        throws AssertionError: If test case fails
        System test for stop punctuation
        """
        input_fname = "../../test-plans/Plaintext/Stop-Punctuation/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Plaintext/Stop-Punctuation/output.txt"
        actual_output_fname = "../../test-plans/Plaintext/Stop-Punctuation/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_stop_words(self):
        """
        throws AssertionError: If test case fails
        System test for stopwords
        """
        input_fname = "../../test-plans/Plaintext/Stop-Words/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Plaintext/Stop-Words/output.txt"
        actual_output_fname = "../../test-plans/Plaintext/Stop-Words/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_whitespace(self):
        """
        throws AssertionError: If test case fails
        System test for stopwords
        """
        input_fname = "../../test-plans/Plaintext/Whitespace/input.txt"
        input_type = "txt"
        expected_output_fname = "../../test-plans/Plaintext/Whitespace/output.txt"
        actual_output_fname = "../../test-plans/Plaintext/Whitespace/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

# ============================================================================
# HTML
# ============================================================================

    def test_html_abbreviated_tags(self):
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

    def test_html_duplicate_metadata(self):
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

    def test_html_duplicate_title(self):
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

    def test_html_inline_css(self):
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

    def test_html_inline_php(self):
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

    def test_html_Internal_css(self):
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

    def test_html_javascript_comments(self):
        """
        throws AssertionError: If test case fails
        System test for javascript comments HTML test plan
        """
        input_fname = "../../test-plans/HTML/Javascript-comments/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Javascript-comments/output.txt"
        actual_output_fname = "../../test-plans/HTML/Javascript-comments/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_meta_title(self):
        """
        throws AssertionError: If test case fails
        System test for meta title HTML test plan
        """
        input_fname = "../../test-plans/HTML/Meta-title/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Meta-title/output.txt"
        actual_output_fname = "../../test-plans/HTML/Meta-title/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_multiline_comments(self):
        """
        throws AssertionError: If test case fails
        System test for multiline comments HTML test plan
        """
        input_fname = "../../test-plans/HTML/Multi-Line-Comments/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Multi-Line-Comments/output.txt"
        actual_output_fname = "../../test-plans/HTML/Multi-Line-Comments/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_nested_html_comments(self):
        """
        throws AssertionError: If test case fails
        System test for nested html comments HTML test plan
        """
        input_fname = "../../test-plans/HTML/Nested-html-comments/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Nested-html-comments/output.txt"
        actual_output_fname = "../../test-plans/HTML/Nested-html-comments/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_no_meta_tags(self):
        """
        throws AssertionError: If test case fails
        System test for no meta tags HTML test plan
        """
        input_fname = "../../test-plans/HTML/No-meta-tags/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/No-meta-tags/output.txt"
        actual_output_fname = "../../test-plans/HTML/No-meta-tags/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_no_title(self):
        """
        throws AssertionError: If test case fails
        System test for no title HTML test plan
        """
        input_fname = "../../test-plans/HTML/No-title/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/No-title/output.txt"
        actual_output_fname = "../../test-plans/HTML/No-title/actual.txt"

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

    def test_html_script_tags(self):
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

    def test_html_single_line_comments(self):
        """
        throws AssertionError: If test case fails
        System test for single line comments HTML test plan
        """
        input_fname = "../../test-plans/HTML/Single-Line-Comments/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Single-Line-Comments/output.txt"
        actual_output_fname = "../../test-plans/HTML/Single-Line-Comments/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_special_characters(self):
        """
        throws AssertionError: If test case fails
        System test for special characters HTML test plan
        """
        input_fname = "../../test-plans/HTML/Special-Characters/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Special-Characters/output.txt"
        actual_output_fname = "../../test-plans/HTML/Special-Characters/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_tags(self):
        """
        throws AssertionError: If test case fails
        System test for tags HTML test plan
        """
        input_fname = "../../test-plans/HTML/Tags/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Tags/output.txt"
        actual_output_fname = "../../test-plans/HTML/Tags/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_html_title_meta_title(self):
        """
        throws AssertionError: If test case fails
        System test for title / meta title HTML test plan
        """
        input_fname = "../../test-plans/HTML/Title-meta-title/input.txt"
        input_type = "html"
        expected_output_fname = "../../test-plans/HTML/Title-meta-title/output.txt"
        actual_output_fname = "../../test-plans/HTML/Title-meta-title/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

# ============================================================================
# MARKDOWN
# ============================================================================

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

    def test_md_inline_image_with_extra(self):
        """
        throws AssertionError: If test case fails
        System test for inline image with extra md test plan
        """
        input_fname = "../../test-plans/Markdown/Inline-Image-with-extra/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Inline-Image-with-extra/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Inline-Image-with-extra/actual.txt"

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

    def test_md_inline_line_style_with_extra(self):
        """
        throws AssertionError: If test case fails
        System test for inline image with extra md test plan
        """
        input_fname = "../../test-plans/Markdown/Inline-Link-Style-with-extra/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Inline-Link-Style-with-extra/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Inline-Link-Style-with-extra/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_multi_tick_code_blocks(self):
        """
        throws AssertionError: If test case fails
        System test for multi tick code blocks md test plan
        """
        input_fname = "../../test-plans/Markdown/Multi-Tick-Code-Blocks/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Multi-Tick-Code-Blocks/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Multi-Tick-Code-Blocks/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_numbered_reference_style_link(self):
        """
        throws AssertionError: If test case fails
        System test for numbered reference style link md test plan
        """
        input_fname = "../../test-plans/Markdown/Numbered-Reference-Style-Link/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Numbered-Reference-Style-Link/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Numbered-Reference-Style-Link/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_reference_image(self):
        """
        throws AssertionError: If test case fails
        System test for reference image md test plan
        """
        input_fname = "../../test-plans/Markdown/Reference-Image/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Reference-Image/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Reference-Image/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_reference_image_with_extra(self):
        """
        throws AssertionError: If test case fails
        System test for reference image with extra md test plan
        """
        input_fname = "../../test-plans/Markdown/Reference-Image-with-extra/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Reference-Image-with-extra/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Reference-Image-with-extra/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_reference_style_link(self):
        """
        throws AssertionError: If test case fails
        System test for reference style link md test plan
        """
        input_fname = "../../test-plans/Markdown/Reference-Style-Link/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Reference-Style-Link/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Reference-Style-Link/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_relative_repository_reference_link(self):
        """
        throws AssertionError: If test case fails
        System test for relative repository reference link md test plan
        """
        input_fname = "../../test-plans/Markdown/Relative-Repository-Reference-Link/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Relative-Repository-Reference-Link/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Relative-Repository-Reference-Link/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_self_reference_style_link(self):
        """
        throws AssertionError: If test case fails
        System test for self reference style link md test plan
        """
        input_fname = "../../test-plans/Markdown/Self-Reference-Style-Link/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Self-Reference-Style-Link/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Self-Reference-Style-Link/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)

    def test_md_single_tick_code_blocks(self):
        """
        throws AssertionError: If test case fails
        System test for single tick code blocks md test plan
        """
        input_fname = "../../test-plans/Markdown/Single-Tick-Code-Blocks/input.txt"
        input_type = "md"
        expected_output_fname = "../../test-plans/Markdown/Single-Tick-Code-Blocks/output.txt"
        actual_output_fname = "../../test-plans/Markdown/Single-Tick-Code-Blocks/actual.txt"

        # Run the test!
        self.run_test_check_output(input_fname, input_type,
                                   expected_output_fname, actual_output_fname)


if __name__ == "__main__":
    unittest.main()
