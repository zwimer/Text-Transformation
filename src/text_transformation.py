"""
This file contains the main system code for running text transformation.
"""

import sys
import os
import json
import requests

import html_sanitizer
import markdown_sanitizer
import text_sanitizer
import ngram_creator


# easy print to error
# code from stackoverflow:
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def arg():
    """
    returns: filename (string) and file_type (string, assumed to be 'txt',
        'html', or 'md')
    """
    # Get filename and type from CLI
    if len(sys.argv) != 4:
        eprint("ERROR: (text_t) Invalid usage:\nUSAGE: python3 " + sys.argv[0]
               + " <file name> <file type> [optional output file]\n" +
               "Valid file extensions are: 'txt', 'md', 'html'")
        sys.exit()

    filename = sys.argv[1]
    file_type = sys.argv[2]
    url = sys.argv[3]

    return filename, file_type, url


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
    elif file_type == "txt" or file_type == "pdf":
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
    # eprint("LOG:\t(text_t)\tRequesting stop words from server")

    # TODO this is temporary, use real address
    r = requests.get("http://teamq.cs.rpi.edu:8080/stopWords")
    try:
        stopwords = r.json()
        eprint("LOG:\t(text_t)\tReceived stop words from server")
    except Exception as e:
        eprint("ERROR: Failed to get stopwords from server")
        sys.exit()

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
    if len(arguments) != 3:
        eprint("ERROR: Invalid usage\nCommand line usage: "
               "python3 text_transformation.py"
               "<file name> <file type> [optional output file]\n"
               "Valid file extensions are: 'txt', 'md', 'html'")
        sys.exit()

    filename, file_type, url = arguments

    # eprint("LOG:\t(text_t)\tfilename:", filename,
    # "\n\t\t\tfile type:", file_type)

    types_allowed = ("txt", "pdf", "md", "html")

    if file_type not in types_allowed:
        eprint("ERROR: Unusable file type")
        sys.exit()

    # Open and read in file
    try:
        f = open(filename, "r", encoding="utf-8")
    except Exception as e:
        eprint("ERROR: File failed to open")
        f.close()
        sys.exit()

    # Get text, then remove file
    text = f.read()
    f.close()
    os.remove(filename)

    # eventual full output dictionary
    output = {}

    # parse text
    # eprint("LOG:\t(text_t)\tParsing data")
    (title, metadata, text_list) = parse(text, file_type)

    # Get ngrams and add to output
    output["ngrams"] = get_ngrams(text_list)

    # metadata will either be populated or an empty dictionary
    output["metadata"] = metadata

    # title is either a string or none
    output["title"] = {"title": title}
    output["title"]["indices"] = get_title_indices(title, output["ngrams"][1])

    output["url"] = url
    # eprint("LOG:\t(text_t)\tCreated json output object")

    # If sending to server:
    headers = {"Accept": "application/json",
               "Content-Type": "text/plain"}
    data = json.dumps(output)

    eprint("LOG:\t(text_t)\tSending json output to server")

    # TODO: real server request pls
    r = requests.post("http://teamq.cs.rpi.edu:8080/setToken",
                      data=data, headers=headers)
    eprint("LOG:\t(text_t)\tServer response:", r.status_code, r.text)


if __name__ == "__main__":
    main(arg())
    # TODO connection from crawling?
