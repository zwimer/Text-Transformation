import string
import plaintext_parser
import re

class MarkdownParser:
    def __init__(self):
        """
            The constructor. No initialization is needed for this parser.
        """

    # Input: Giant string of markdown content
    # Output: List of list of strings (lower cased individual words)
    def parse(self, content):
        # Remove all code blocks
        code_blocks = r'`(.*?(\s)*?)*?`'
        code_free_content = re.sub(code_blocks, " ", content)

        # Remove links (this will include image blocks--the ! symbol is removed
        # by plaintext later on)
        link_blocks = r'\[(.*?)\][\[\(].*?[\]\)]'
        regex = re.compile(link_blocks)
        new_content = regex.sub("\\1", code_free_content)
        
        # May need to go line by line to feed into plaintext_parser here...
        PTParser = plaintext_parser.PlaintextParser()
        return PTParser.parse(new_content)
