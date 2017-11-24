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


def json_to_str(text):
    """
    :param text: The text to convert
    :returns: text as a json
    Standardize method of converting from json to a string for testing
    """
    return json.dumps(text, indent=4, separators=(',', ':'))


class TestHtmlSanitizer(unittest.TestCase):
    """
    This class is used to test the html parser class
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
        self.assertEquals(type(expected), type(actual))

        # If the types are jsons, make them strings
        if type(actual) is [ list, dict ]:
            expected = json_to_str(expected)
            actual = json_to_str(actual)

        # Test to ensure equality
        try:
            self.assertEquals(actual, expected)

        # If the assertion fails
        except AssertionError:
            print '*** Assertion failed! ***'
            print 'Actual:' + str(actual)
            print 'Expected:' + str(expected)
            print '*** Re-emitting error ***'
            raise

    def run_test_check_output(self, input_data, expected_output):
        """
        :param input_data: The data to be input to the parser
        :param expected_output: The expected output of the parser
        :throws AssertionError: if test fails
        :returns: nothing
        Test that the extracted output matches the expected
        """
        parser = HtmlSanitizer(input_data)
        output = parser.extract_plain_text_lists()
        self.assert_equality(expected_output, output)

    def run_test_check_metadata(self, input_data, expected_metadata):
        """
        :param input_data: The data to be input to the parser
        :param expected_metadata: The expected metadata collected by the parser
        :throws AssertionError: if test fails
        :returns: nothing
        Test that the extracted metadata matches the expected
        """
        parser = HtmlSanitizer(input_data)
        metadata = parser.get_metadata()
        self.assert_equality(expected_metadata, metadata)

    def run_test_check_title(self, input_data, expected_title):
        """
        :param input_data: The data to be input to the parser
        :param expected_title: The expected title collected by the parser
        :throws AssertionError: if test fails
        :returns: nothing
        Test that the extracted title matches the expected
        """
        parser = HtmlSanitizer(input_data)
        title = parser.get_title()
        self.assert_equality(expected_title, title)

    def run_test_check_sanitized(self, input_data, expected_title):
        """
        :param input_data: The data to be input to the parser
        :param expected_title: The expected title collected by the parser
        :throws AssertionError: if test fails
        :returns: nothing
        Test that the extracted sanitized strings match the expected
        """
        parser = HtmlSanitizer(input_data)
        sanitized_strs = parser.sanitize()
        self.assert_equality(expected_title, sanitized_strs)

    def test_general_words(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        General test case for output
        """

        # Test input and expected output
        html = ('<title> My Amazing book </title>\n'
                '<meta name="author" content="Meg">\n'
                'Hello World book')
        output = [' My Amazing book ', '\n', '\nHello World book']

        # Test the parser
        self.run_test_check_output(html, output)

    def test_general_metadata(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        General test case for metadata
        """

        # Test input and expected metadata
        html = ( '<title> My Amazing book </title>\n'
                 '<meta name="author" content="Meg">\n'
                 'Hello World book' )
        metadata = {'author' : 'meg'}

        # Test the parser
        self.run_test_check_metadata(html, metadata)

    def test_general_title(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        General test case for title
        """

        # Test input and expected title
        html = ( '<title> My Amazing book </title>\n'
                 '<meta name="author" content="Meg">\n'
                 'Hello World book' )
        title = ' my amazing book '

        # Test the parser
        self.run_test_check_title(html, title)

    def test_general_2(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        General test case
        """

        # Test input and all expected outputs
        html = ('<p> Hello World book\n'
                'banana\n'
                '\n'
                'apple bub </p> Bill\n'
                '\n'
                '<title> My Amazing book </title>\n'
                '<meta name="author" content="Meg"> Meg')
        output = [
            ' Hello World book\nbanana\n\napple bub ',
            ' Bill\n\n',
            ' My Amazing book ',
            '\n',
            ' Meg'
        ]
        sanitized_output = [
            'hello world book banana apple bub',
            'bill',
            'my amazing book',
            '',
            'meg'
        ]
        metadata = {'author' : 'meg'}
        title = ' my amazing book '

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)
        # TODO: self.run_test_check_sanitized(html, sanitized_output)

    def test_duplicate_metadata(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test duplicate metadata
        """

        # Test input and all expected outputs
        html = ('<meta name="author" content="Bob"> Bob\n'
                '<title> My Amazing book </title>\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = [' Bob\n', ' My Amazing book ',
                  '\n', ' Meg\nHello World book']
        metadata = {'author' : 'bob'}
        title = ' my amazing book '

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_duplicate_title(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test duplicate title tags
        """

        # Test input and all expected outputs
        html = ('<title> Hi </title>\n'
                '<title> My Amazing book </title>\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = [' Hi ', '\n', ' My Amazing book ',
                  '\n', ' Meg\nHello World book']
        metadata = {'author' : 'meg'}
        title = ' hi '

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_meta_title_tag(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test meta title tags
        """

        # Test input and all expected outputs
        html = ('<meta name="title" content="My Amazing book"> My Amazing book\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = [' My Amazing book\n', ' Meg\nHello World book']
        metadata = {'author' : 'meg'}
        title = 'my amazing book'

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_title_and_meta_title_taga(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test what happens if both title and meta-title tags exist
        """

        # Test input and all expected outputs
        html = ('<meta name="title" content="Hi"> Hi\n'
                '<title> My Amazing book </title>\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = [' Hi\n', ' My Amazing book ', '\n', ' Meg\nHello World book']
        metadata = {'author' : 'meg'}
        title = ' my amazing book '

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_no_metadata(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test when metadata should be empty
        """

        # Test input and all expected outputs
        html = ('<title> My Amazing book </title>\n'
                'Hello World book')
        output = [' My Amazing book ', '\nHello World book']
        metadata = {}
        title = ' my amazing book '

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_no_title(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test when title should be None
        """

        # Test input and all expected outputs
        html = ('<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = [' Meg\nHello World book']
        metadata = {'author' : 'meg'}
        title = None

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_remove_single_line_comments(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html single line comments
        """

        # Test input and all expected outputs
        html = ('<!-- This should be ignored -->\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = ['\n', ' Meg\nHello World book']
        metadata = {'author' : 'meg'}
        title = None

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_remove_multi_line_comments(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes html multi line comments
        """

        # Test input and all expected outputs
        html = ('<!-- This should be\n'
                'ignored -->\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book\n')
        output = ['\n', ' Meg\nHello World book\n']
        metadata = {'author' : 'meg'}
        title = None

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_remove_javascript(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes javascript
        """

        # Test input and all expected outputs
        html = ('<script>\n'
                'Everything here should be ignored\n'
                '</script>\n'
                '<script src = "This too"> Should be removed </script>\n'
                '<script/>\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book\n')
        output = ['\n', '\n', '\n', ' Meg\nHello World book\n']
        metadata = {'author' : 'meg'}
        title = None

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_remove_inline_css(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes inline CSS
        """

        # Test input and all expected outputs
        html = ('<h1 style="color:blue;margin-left:30px;"></h1> Meg\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = [' Meg\n', ' Meg\nHello World book']
        metadata = {'author' : 'meg'}
        title = None

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_remove_internal_css(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser removes internal CSS
        """

        # Test input and all expected outputs
        html = ('<style>\n'
                'body {\n'
                'background-color: linen;\n'
                '}\n'
                '\n'
                'h1 {\n'
                'color: maroon;\n'
                'margin-left: 40px;\n'
                '}\n'
                '</style>\n'
                '<meta name="author" content="Meg"> Meg\n'
                'Hello World book')
        output = ['\n', ' Meg\nHello World book']
        metadata = {'author' : 'meg'}
        title = None

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

    def test_replace_special_chars(self):
        """
        :throws AssertionError: If test case fail
        :returns: nothing
        Test that the parser replaces special characters with what they represent
        For example: '&lt;' should be replaced with '<'
        """

        # Test input and all expected outputs
        html = ('<meta name="author" content="Meg"> Meg\n'
                'Hello World &lt; book')
        output = [' Meg\nHello World < book']
        metadata = {'author' : 'meg'}
        title = None

        # Test the parser
        self.run_test_check_output(html, output)
        self.run_test_check_metadata(html, metadata)
        self.run_test_check_title(html, title)

# Do not run on imports
if __name__ == '__main__':
    unittest.main()
