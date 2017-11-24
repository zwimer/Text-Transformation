"""
This file contains the class TextSanitizer.
This file is meant to hold a text sanitization class
to extract the plain text from its input. This class also 
exposes methods which allow the extraction of metadata and 
the title of the input.
"""

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
        Each string represents a contiguous set of words not interrupted by stop-tags
        """

        # Convert the text to plain text then sanitize the text
        text_lists = self.extract_plain_text_lists()
        ret = []
        _ = [ ret.extend(self.sanitize_plain_text(i)) for i in text_lists ]
        return ret
        
    def extract_plain_text(self):
        """
        :returns: The lists of plain text found
        """
        return [ self.input ] 

    @staticmethod
    def sanitize_plain_text(dirty):
        """
        :param dirty: The unclean text that must be sanitized
        :returns: Sanitized plain text of dirty
        """

        # TODO: TODO !!!!!
        return [ str(dirty.lower()) ]
