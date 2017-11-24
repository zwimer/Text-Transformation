"""
This file contains the class HtmlSanitizer.
This file is meant to sanitize html to extract the plain
text it represents. This class also exposes methods which
allow the extraction of metadata and the title of the html.
"""

from text_sanitizer import TextSanitizer

from bs4 import BeautifulSoup, Comment
import random
import string
import re


def create_delimiter(text):
    """
    :param text: The text to create a delimiter for
    :returns: A delimiter not in text
    Create a delimiter that does not exist in text
    """

    # Construct an initial delimiter
    delimiter = random.choice(string.printable)

    # While the delimiter exists in text, add random characters to it
    while delimiter in text:
        delimiter += random.choice(string.printable)

    # Return the resulting delimiter
    return delimiter

def uniform_sanitize(in_data):
    """
    :param in_data: The data to be sanitized as a string
    :returns: in_text sanitized by TextSanitizer
    A uniform method that HtmlSanitizer can use to sanitize 
    plain text and get a string as a result
    """
    return ' '.join(TextSanitizer.sanitize_plain_text(str(in_data)))


class HtmlSanitizer(TextSanitizer):
    """
    This class is a TextSanitizer which also sanitizes html
    It exposes interfaces allowing both title extraction and metadata extraction
    Note: This class assumes meta title tags and unnamed tags are not metadata
    """

    def __init__(self, html):
        """
        :param html: The html to be parsed
        The constructor
        """

        # Create the internal html parser
        self.soup = BeautifulSoup(html, 'html.parser')

        # Determine a unique delimiter not in input_html
        self.delimiter = create_delimiter(html)

        # A set of functions which must be run before extraction of words
        self.must_run_before_extract = [
            self.clear_comments,
            self.clear_code
        ]

    def get_metadata(self):
        """
        :returns: A dict of metadata tags whose names are mapped to their sanitized content
        Extracts metadata from the html stored in soup.
        Note: meta title tags and unnamed tags are not considered metadata
        """

        # All known metadata
        metadata = {}

        # For each tag of type tag_name in soup that has a name and content
        for tag in self.soup.find_all('meta', attrs={'name': True, 'content': True}):
            tag_name = str(tag['name'])

            # Skip meta title tags or unnamed tags
            if tag_name == 'title':
                continue

            # Add next meta tag's sanitized content field to the dict
            if tag_name not in metadata:
                content = str(tag['content'])
                metadata[tag_name] = uniform_sanitize(content)

        # Return metadata
        return metadata

    def get_title(self):
        """
        :returns: Sanitized title of the self.soup. If none was found, return None
        Secondarily checks meta title tags if no titles tags were found.
        """

        # First search title tags
        for tag in self.soup.find_all('title'):
            return uniform_sanitize(' '.join(tag.contents))

        # If no title tags were found, search for meta title tags that have content
        for tag in self.soup.find_all('meta', attrs={'name': 'title', 'content': True}):
            return uniform_sanitize(tag['content'])

        # If no title tags were found, return None
        return None

    def extract_plain_text_lists(self):
        """
        :returns: The plain text stored in the html of self.soup as a list of strings
        Each string represents a contiguous section of the plain text of the html
        The strings are split where tags were.
        Note: Special characters are replaced with what they represent
        """

        # For all functions which must run first, run them
        while len(self.must_run_before_extract) > 0:
            self.must_run_before_extract[0]()

        # Extract the text, place delimiter where tags used to be
        extracted_text = str(self.soup.get_text(self.delimiter, strip=False))

        # Return the extracted text as a list
        return extracted_text.split(self.delimiter)

    def clear_comments(self):
        """
        :returns: nothing
        Clear comments in the html stored in self.soup
        """

        # Create a function to identify comments
        def is_comment(text): return isinstance(text, Comment)

        # Remove all comments
        for comment in self.soup.findAll(text=is_comment):
            self.clear_tag(comment)

        # This function has already run, so it no longer has to be run
        self.must_run_before_extract.remove(self.clear_comments)

    def clear_code(self):
        """
        :returns: nothing
        Clear all code tags in the html stored in self.soup
        """

        # Types of tags which store code
        code_tags = ['script', 'style']

        # Remove all code tags
        for tag_name in code_tags:
            for tag in self.soup(tag_name):
                self.clear_tag(tag)

        # This function has already run, so it no longer has to be run
        self.must_run_before_extract.remove(self.clear_code)

    def clear_all_tags_of_name(self, tag_name):
        """
        :param tag: The tag to be removed
        :returns: nothing
        Clear all tags of type tag in the html stored in self.soup
        """

        # For each tag of tpye tag_name in soup, remove it
        for next_tag in self.soup.find_all(tag_name):
            self.clear_tag(next_tag)

    def clear_tag(self, tag):
        """
        :param tag: The tag to be cleared
        :returns: nothing
        """

        # Determine the tag name
        tag_name = (tag.name if tag.name is not None else '')

        # Clear the tag
        tag.replace_with(self.soup.new_tag(tag_name))
