"""
This file contains the main system code for running text transformation.
"""

import sys
import json

import html_sanitizer
import markdown_sanitizer
import text_sanitizer
import ngram_creator


def arg():
    """
    returns: filename (string) and file_type (string, assumed to be 'txt',
        'html', or 'md')
    """
    # Get filename and type from CLI
    if len(sys.argv) != 3:
        print("USAGE: python3 script filename file_type")
        sys.exit()

    filename = sys.argv[1]
    file_type = sys.argv[2]

    return filename, file_type


def parse(text, file_type):
    """
    param text: full text to be parsed
    returns a tupe with (title string, metadata dictionary, parsed text lists)
    """

    # Create parser based on file type
    if file_type == "html":
        parser = html_sanitizer.HtmlSanitizer(text)
    elif file_type == "md":
        parser = markdown_sanitizer.MarkdownSanitizer(text)
    elif file_type == "txt":
        parser = text_sanitizer.TextSanitizer(text)

    return (parser.get_title(), parser.get_metadata(), parser.sanitize())


def get_title_indices(title, onegrams):
    """
    param title: the title string (can be None)
    param onegrams: The dictionary of onegrams and their indices created
        by ngram_creator
    returns: a list of the title's indices
    """

    # no title -> return an empty list
    if title is None:
        return []

    title_terms = title.split()
    current = 0
    queue = set()
    queue.add(())
    indices = []

    # Constructs a set of all viable index "paths" that the title is found at
    while (current != len(title_terms)):
        newqueue = set()

        for index in onegrams[title_terms[current]]:
            # Add this to the queue if it is a continuation of a title "path"
            for path in queue:
                if len(path) == 0 or path[-1] == index - 1:
                    newqueue.add(path + (index,))

        # move on to the next term
        queue = newqueue
        current += 1

    for path in queue:
        indices.append(path[0])

    return indices


def get_ngrams(text):
    """
    param text: list of lists of strings used for ngram creation
    returns: a dictionary of ngrams and their indices, divided by number
        of terms
    """
    # Get stopwords from indexing
    # TODO add call to indexing

    # stopwords_fname = "temp/english_stopwords.json"
    # stopwords = json.load( open(stopwords_fname, "r") )

    stopwords = ["couch"]

    # Compile ngram_creator's results
    return {1: ngram_creator.create(text, 1, stopwords, False),
            2: ngram_creator.create(text, 2, stopwords, True),
            3: ngram_creator.create(text, 3, stopwords, True)}

# =============================================================================
# MAIN
# =============================================================================


def main(arguments, output_fname=None):
    """
    param arguments: a tuple containing the name of the file to be used and
        its type. Allowable types are 'txt', 'html', or 'md'.
    """

    # Check for validity
    if len(arguments) != 2:
        print("ERROR: arguments must be filename, file_type")
        sys.exit()

    # TODO this will come from a different source eventually
    filename = arguments[0]
    file_type = arguments[1]

    types_allowed = ("txt", "md", "html")

    if file_type not in types_allowed:
        print("ERROR: Unusable file type")
        sys.exit()

    # Open and read in file
    try:
        f = open(filename, "r", encoding="utf-8")
    except Exception as e:
        print("ERROR: File failed to open")
        f.close()
        sys.exit()

    text = f.read()
    f.close()

    # eventual full output dictionary
    output = {}

    # parse text
    (title, metadata, text_list) = parse(text, file_type)
    # TODO remove dummy values
    # text_list = [["my", "amazing", "book"], ["hello", "world", "book"]]
    # title = "my amazing book"

    # Get ngrams and add to output
    output["ngrams"] = get_ngrams(text_list)

    # metadata will either be populated or an empty dictionary
    output["metadata"] = metadata

    # title is either a string or none
    output["title"] = {"title": title}
    output["title"]["indices"] = get_title_indices(title, output["ngrams"][1])

    # Write to file as JSON
    if output_fname is None:
        output_fname = "dummy.json"
    # TODO output file name should be programmatically generated
    try:
        fout = open(output_fname, "w")
    except Exception as e:
        print("ERROR: Output file creation failed")
        sys.exit()

    json.dump(output, fout, sort_keys=True, indent=4,
              separators=(',', ':'))
    fout.close()


if __name__ == "__main__":
    main(arg())
    # TODO connection from crawling?
