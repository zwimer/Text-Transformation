import string
import plaintext_parser
import re

class MarkdownParser:
    def __init__(self):
        """
            The constructor. No initialization is needed for this parser.
        """

    # Input: Giant string of markdown content
    # Outblockput: List of list of strings (lower cased individual words)
    def parse(self, content):
        # Remove all code blocks
        code_blocks = r'`(.*?(\s)*?)*?`'
        new_content = re.sub(code_blocks, " ", content)

        # May need to go line by line to feed into plaintext_parser here...
        PTParser = plaintext_parser.PlaintextParser()
        return PTParser.parse(new_content)
