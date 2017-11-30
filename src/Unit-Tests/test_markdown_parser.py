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

# TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
class TestMarkdownSanitizer(unittest.TestCase):
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
        parser = MarkdownSanitizer(input_data)
        output = parser.extract_plain_text_lists()

        self.assert_equality(expected_output, output)

    def test_inline_image(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('\"Click ![here](www.freestuff.com/image_link) for free stuff\"\n')
        output = ['\n\"Click !here for free stuff\"\n\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_inline_image_extra(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('\"Click ![here](www.freestuff.com/image_link \"Title goes here\") for free stuff\"')
        output = ['\n\"Click !here for free stuff\"\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_inline_style(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('Click [here](www.freestuff.com) for free stuff')
        output = ['\nClick here for free stuff\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_inline_style_extra(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('Click [here](www.freestuff.com FreeStuffTitle) for free stuff')
        output = ['\nClick here for free stuff\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_multi_tick_code_blocks(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('we ignore this ```printf("this is code\n")``` great')
        output = ['\nwe ignore this     great\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_numbered_reference_style_link(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('\"Click [here][1] for free stuff\"\n\n[1]: https://www.google.com')
        output = ['\"Click here for free stuff\"\n\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_numbered_reference_style_link(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('\"Click [here][logo] for free stuff\"\n\n[logo]: https://www.google.com/my_image')
        output = ['\n\"Click here for free stuff\"\n\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_numbered_reference_style_link_extra(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('\"Click [here][logo] for free stuff\"\n\n[logo]: https://www.google.com/my_image "Title"\n Banana \n[2]: dfsdfds\n[3]: t')
        output = ['\n\"Click here for free stuff\"\n\n Banana \n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_relative_repository(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('Click [here](../Free/Stuff) for free stuff')
        output = ['\nClick here for free stuff\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

    def test_single_tick_code_blocks(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        md = ('we ignore this `printf("this is code\n")` great')
        output = ['\nwe ignore this   great\n']
        metadata = None
        title = None

        # Test the parser
        self.run_test_check_output(md, output)

# Do not run on imports
if __name__ == '__main__':
    unittest.main()
