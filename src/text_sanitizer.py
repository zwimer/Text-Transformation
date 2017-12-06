"""
This file contains the class TextSanitizer.
This file is meant to hold a text sanitization class
to extract the plain text from its input. This class also
exposes methods which allow the extraction of metadata and
the title of the input.
"""

import re
import string


class TextSanitizer:
    """
    This class is meant to sanitize plain text.
    It provides an interface for extracting metadata and a title
    which can be overridden by subclasses.
    """

    def __init__(self, to_sanitize):
        """
        :param to_sanitize: The text to sanitize
        The constructor
        """
        self.input = to_sanitize

    def get_metadata(self):
        """
        :returns: The metadata extracted from self.input
        """
        return {}

    def get_title(self):
        """
        :returns: The title extracted from self.input
        """
        return None

    def sanitize(self):
        """
        :returns: Sanitized text extracted from input as a list of strings
        Each string represents a contiguous set of words not interrupted by
        stop-tags
        """

        # Convert the text to plain text then sanitize the text
        text_lists = self.extract_plain_text_lists()
        ret = []
        _ = [ret.extend([i.split() for i in self.sanitize_plain_text(i)])
             for i in text_lists]
        return ret

    def extract_plain_text_lists(self):
        """
        :returns: The lists of plain text found
        """
        return [self.input]

    @staticmethod
    def sanitize_plain_text(dirty):
        """
        :param dirty: The unclean text that must be sanitized
        :returns: Sanitized plain text of dirty
        This is the bread and butter function that will strip
        symbols and punctuation from the input string.
        """

        # Lower case all words
        dirty = str(dirty).lower()

        # Remove all symbols except # > (stop punctuation)
        # Remove all symbols except ' - (words w/ contractions)
        removable_punct = re.sub("[#>\'-]", "", string.punctuation)
        translator = str.maketrans("", "", removable_punct)
        parsed = dirty.translate(translator)

        # First, need to split into "blocks" on stop punctuation
        # (except html tags; this is done by HTML parser)
        stop_punct = "\n\t|\n\n|\n\#|\n>"
        block_list = re.split(stop_punct, parsed)

        # Second, need to "clean" out extraneous # and >
        # that were not part of stop punctuation from each block
        clean_block_list = []
        translator = str.maketrans("", "", "#>")
        clean_block_list = [block.translate(translator)
                            for block in block_list]

        # Remove invalid apostrophes/hyphens that are not apart of a word
        invalid_contractions = "\'\s+|\s+\'|-\s+|\s+-"
        new_block_list = [re.sub(invalid_contractions, " ", block)
                          for block in clean_block_list]

        # Strip whitespace from each block and remove empty blocks
        new_block_list = [i.strip() for i in new_block_list]
        new_block_list = [i for i in new_block_list if i]

        # Finally, in each block, replace all
        # contiguous chunks of whitespace with a single ' '
        sanitized_blocks = [' '.join(i.split()) for i in new_block_list]

        # Return the list as a list of strings
        return [str(i) for i in sanitized_blocks]
