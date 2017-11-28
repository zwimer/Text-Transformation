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

    print("DEBUG:\tFilename:\t{}\n\tFile type:\t{}" \
        .format(filename, file_type) )

    return filename, file_type

def parse(text, file_type):
    """
    param text: full text to be parsed
    returns a tupe with (title string, metadata dictionary, parsed text lists)
    """

    print("DEBUG: Parsing as {}".format(file_type))

    # Create parser based on file type
    if file_type == "html":
        parser = html_sanitizer.HtmlSanitizer(text)
    elif file_type == "md":
        parser = markdown_sanitizer.MarkdownSanitizer(text)
    elif file_type == "txt":
        parser = text_sanitizer.TextSanitizer(text)

    return (parser.get_title(), parser.get_metadata(), parser.sanitize())

def get_title_indices(title, text_lists):
    """
    param title: the title string (can be None)
    param text_lists: list of list of strings of sanitized text
    returns: a list of indices where the title is found in the text
    """

    # no title -> return an empty list
    if title == None:
        return []

    # Count the term index
    index = 0
    indices = []

    title_terms = title.split()
    title_len = len(title)

    for section in text_lists:

        # if the start of the title isn't in this section, skip it
        if not title_terms[0] in section:
            index += len(section)
            continue

        for term, i in enumerate(section):
            if term == title_terms[0]:

                # when the first term is found, check the title_terms list
                # against a sublist from section of the same length as the title
                if title_terms == section[i:i+title_len]:
                    indices.append(index)

            index += 1

    print("DEBUG:\tFound title {} at indices: ".format(title))
    print("\t",indices)

    return indices

def get_ngrams(text):
    """
    param text: list of lists of strings used for ngram creation
    returns: a dictionary of ngrams and their indices, divided by number
        of terms
    """
    # Get stopwords from indexing
    # TODO add call to indexing
    # TODO change for tests
    stopwords_fname = "temp/english_stopwords.json"
    stopwords = json.load( open(stopwords_fname, "r") )

    print("DEBUG:\tLoaded list of {} stopwords".format(len(stopwords)))


    # Compile ngram_creator's results
    return {1 : ngram_creator.create(text, 1, stopwords, False), \
            2 : ngram_creator.create(text, 2, stopwords, True), \
            3 : ngram_creator.create(text, 3, stopwords, True)}

# =============================================================================
# MAIN
# =============================================================================

def main( arguments ):
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

    if not file_type in types_allowed:
        print("ERROR: Unusable file type")
        sys.exit()

    # Open and read in file
    try:
        f = open(filename, "r", encoding="utf-8")
    except:
        print("ERROR: File failed to open")
        sys.exit()

    text = f.read()
    f.close()

    # eventual full output dictionary
    output = {}

    # parse text
    (text_list, metadata, title) = parse(text, file_type)
    # TODO remove dummy values
    text_list = [["my", "amazing", "book"], ["hello", "world", "book"]]
    title = "my amazing book"

    # metadata will either be populated or an empty dictionary
    output["metadata"] = metadata

    # title is either a string or none
    output["title"] = { "title" : title }
    output["title"]["indices"] = get_title_indices(title, text_list)

    # Get ngrams and add to output
    output["ngrams"] = get_ngrams(text_list)

    # Write to file as JSON
    # TODO output file name should be programmatically generated
    try:
        fout = open("dummy.json", "w")
    except:
        print("ERROR: Output file creation failed")
        sys.exit()

    json.dump(output, fout, sort_keys=True, indent=4, \
        separators=(',', ':'))


if __name__ == "__main__":
    main(arg())
    # TODO connection from crawling?
