"""
This file contains the function parse(content).
This function removes extraneous symbols/stop punctuation from content and
returns a list of lists of words, where each list of words is a
contiguous set of words not interrupted by certain stop punctuation.
"""

import string
import re

class PlaintextParser:
    """
    This class allows the client to strip extraneous syntax from an input
    string such as symbols and punctuation.
    It has the ability to extract metadata from an input string, although this
    feature is not fully defined.
    """

    def __init__(self):
        """
            The constructor. No initialization is needed for this parser.
        """

    def parse(self, content):
        """
            :param content: One string of plaintext content
            :returns: List of list of strings (lower cased individual words)
            This is the bread and butter function that will strip
            symbols and punctuation from the input string.
        """

        # Lower case all words
        content = content.lower()

        # Remove all symbols except # > (stop punctuation)
        # Remove all symbols except ' - (words w/ contractions)
        removable_punct = re.sub("[#>\'-]", "", string.punctuation)
        translator = str.maketrans("", "", removable_punct)
        parsed = content.translate(translator)

        # First, need to split into "blocks" on stop punctuation
        # (except html tags; this is done by HTML parser)
        stop_punct = "\n\t|\n\n|\n\#|\n>"
        block_list = re.split(stop_punct, parsed)

        # Second, need to "clean" out extraneous # and >
        # that were not part of stop punctuation from each block
        clean_block_list = []
        translator = str.maketrans("", "", "#>")
        clean_block_list = [block.translate(translator) for block in block_list]

        # Remove invalid apostrophes/hyphens that are not apart of a word
        invalid_contractions = "\'\s+|\s+\'|-\s+|\s+-"
        new_block_list = [re.sub(invalid_contractions, " ", block) for block in clean_block_list]

        # Finally, split on whitespace to get individual words
        list_of_lists = [block.split() for block in new_block_list]

        # Clean out empty lists
        list_of_lists = [word_list for word_list in list_of_lists if len(word_list) > 0]

        return list_of_lists

    def parse_metadata(content):
        """
            :param content: One string of plaintext content
            :returns: None
            This is a method stub; metadata is not needed from plaintext files.
        """
        return
