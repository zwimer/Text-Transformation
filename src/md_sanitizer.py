"""
This file contains the class MarkdownParser.
This file is meant to sanitize markdown to extract the plain
text it represents.
"""

import string
import re

class MarkdownParser(TextSanitizer):
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
        code_free_content = re.sub(code_blocks, " ", content)

        # Remove links (this will include image blocks)
        # the ! symbol is sanitized by the parent class later on
        link_blocks = r'\[(.*?)\][\[\(].*?[\]\)]'
        regex = re.compile(link_blocks)
        plain_text = str(regex.sub("\\1", code_free_content))

        # Return the plain text in a list
        return [ result ]
