import string
import plaintext_parser
import re

# Input: Giant string of markdown content
# Output: List of list of strings (lower cased individual words)
# TODO: Need to fix contractions i.e. don't, won't, etc.
def parse(content):
    print("this is original:\n", content)

    # Remove all code blocks
    # TODO

    # May need to go line by line to feed into plaintext_parser here...

    return plaintext_parser.parse(content)
