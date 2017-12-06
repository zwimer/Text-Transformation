"""
This file contains the class MarkdownParser.
This file is meant to sanitize markdown to extract the plain
text it represents.
"""

from text_sanitizer import TextSanitizer

import string
import re

class MarkdownSanitizer(TextSanitizer):
    """
    This class is a TextSanitizer which also sanitizes markdown
    """

    def __init__(self, content):
        """
        :param content: The markdown to sanitize
        The constructor
        """
        self.content = content

    def extract_plain_text_lists(self):
        """
        :returns: The plain text stored in self.content as a list of strings
        Each string represents a contiguous section of the plain text of the markdown
        As markdown contains no 'stop tags', it returns a list with one string.
        """

        # Remove all code blocks
        code_blocks = r'`(.*?(\s)*?)*?`'
        code_free_content = re.sub(code_blocks, " ", self.content)

        # Remove links (this will include image blocks)
        # the ! symbol is sanitized by the parent class later on
        link_blocks = r'\[(.*?)\][\[\(].*?[\]\)]'
        link_regex = re.compile(link_blocks)
        plain_text = str(link_regex.sub("\\1", code_free_content))

        # Remove references
        references = r'\n\[.+\]:.*'
        # references = r'(?:\n|^)\[[\w\s\d]*:[^\n]*(?:\n|$)'
        ref_regex = re.compile(references)
        result = str(ref_regex.sub("", '\n'+plain_text+'\n'))

        # Return the plain text in a list
        return [ result ]
