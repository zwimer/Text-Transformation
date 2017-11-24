import sys
import json

# import Bs4Wrapper <- currently has syntax errors
import plaintext_parser
import md_parser
import ngram_creator

def get_ngrams(text):
    """
    param text: list of lists of strings used for ngram creation
    returns: a dictionary of ngrams and their indices, divided by number
        of terms
    """
    # Get stopwords from indexing
    stopwords = ["my"]

    # Compile ngram_creator's results
    return {1 : ngram_creator.create(text, 1, stopwords, False), \
            2 : ngram_creator.create(text, 2, stopwords, True), \
            3 : ngram_creator.create(text, 3, stopwords, True)}

def parse(text, file_type):
    """
    param text: full text to be parsed
    """
    # Process html files
    if file_type == "html":
        # html_parser = Bs4Wrapper.Bs4Wrapper(text)

        # html_parser.clear_comments()
        # text_lists = html_parser.extract_plain_text_lists():
        pass

    if file_type == "md":
        # markdown parser - needs to be fixed slightly
        # MDParser = md_parser.MarkdownParser()
        # text_lists = MDParser.parse(text)
        pass

    # parse plain text
    # PTParser = plaintext_parser.PlaintextParser()
    # parsed_plaintext_content = PTParser.parse(text_lists)

    return [["my", "amazing", "book"], ["hello", "world", "book"]]

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


def main( arguments ):
    """
    param arguments: a tuple containing the name of the file to be used and
        its type. Type is assumed to be 'txt', 'html', or 'md'.
    """
    filename = arguments[0]
    file_type = arguments[1]

    # Open and read in file
    try:
        f = open(filename, "r")
    except:
        print("ERROR: File failed to open")
        sys.exit()

    text = f.read()
    f.close()

    # eventual full output dictionary
    output = {}

    text_list = parse(text, file_type)

    # figure out division of responsibilities between parse etc for
    # metadata...
    """
    if file_type == "html":
        output["title"] = html_parser.get_title()
        output["metadata"] = html_parser.get_metadata()
        # del metadata if empty
        pass
    else:
        # set title fields to empty
        output["title"] = { "title": "", "indices": [] }
    """
    # Get ngrams and add to output
    output["ngrams"] = get_ngrams(text_list)

    # get title from ngram output

    # Write to file as JSON
    # output file name should be programmatically generated
    try:
        fout = open("dummy.json", "w")
    except:
        print("ERROR: Output file creation failed")
        sys.exit()

    json.dump(output, fout, sort_keys=True, indent=4, \
        separators=(',', ':'))


if __name__ == "__main__":
    main(arg())
