import string
import re

class PlaintextParser:
    """
    This class provides a function for parsing plaintext into a specific format.
    It will also parse the metadata out of a provided
    """

    def __init__(self):
        """
            The constructor. No initialization is needed for this parser.
        """

    def parse(self, content):
        """
            Takes in a string.
            Returns a list of list of strings (lower case individual words)
            Note: If the caller has blocks of strings already
            broken by stopwords (whether it be HTML tags, stop punctuation, or
            otherwise), then the caller must pass each string separately.
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

        return list_of_lists

    def parse_metadata(content):
        """
            This is a method stub; metadata is not needed from plaintext files.
        """
        return
