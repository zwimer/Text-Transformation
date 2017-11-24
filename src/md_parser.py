"""
This file contains the function parse(content).
This function removes markdown specific syntax from content and returns
a list of lists of words, where each list of words is a
contiguous set of words not interrupted by certain stop punctuation denoted in
the PlaintextParser class.
"""

import string
import plaintext_parser
import re

class MarkdownParser:
    """
    This class allows the client to strip markdown specific syntax from an input string.
    It has the ability to extract metadata from an input string, although this
    feature is not fully defined.
    """

    def __init__(self):
        """
            The constructor. No initialization is needed for this parser.
        """

    def parse(self, content):
        """
            :param content: One string of markdown content
            :returns: List of list of strings (lower cased individual words)
            This is the bread and butter function that will strip markdown
            specifics from the input string.
        """
        # Remove all code blocks
        code_blocks = r'`(.*?(\s)*?)*?`'
        code_free_content = re.sub(code_blocks, " ", content)

        # Remove links (this will include image blocks--the ! symbol is removed
        # by plaintext later on)
        link_blocks = r'\[(.*?)\][\[\(].*?[\]\)]'
        regex = re.compile(link_blocks)
        new_content = regex.sub("\\1", code_free_content)

        # TODO: May need to go line by line to feed into plaintext_parser here...
        # This may mean calling super() if we're making plaintext parser the main class
        PTParser = plaintext_parser.PlaintextParser()
        return PTParser.parse(new_content)

    def parse_metadata(content):
        """
            :param content: One string of markdown content
            :returns: None
            This is a method stub; metadata is not needed from markdown files.
        """
        return
