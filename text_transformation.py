import sys

# import Bs4Wrapper <- currently has syntax errors
import plaintext_parser
import md_parser
import ngram_creator

# For preliminary testing
def main(filename, file_type):
    # Raw input comes into text_transformation

    # If input is html, call html_parser here

    # If input is markdown, call md_parser here
    md_content = "# This is a \n\n general Markdown test\n\n```c++\nAnd boy is it ever\n#magic!\n```"
    MDParser = md_parser.MarkdownParser()
    parsed_md_content = MDParser.parse(md_content)
    print("ORIGINAL MD CONTENT:\n", md_content, "\n")
    print("PARSED MD CONTENT:\n", parsed_md_content, "\n")

    # If input is just plaintext:
    plaintext_content = "Break here\n\n. Again, #break-here;\n\tHello World!\nBREAK- HERE \n\# . Don't avoid\n>contractions. James' lol"
    PTParser = plaintext_parser.PlaintextParser()
    parsed_plaintext_content = PTParser.parse(plaintext_content)
    print("ORIGINAL PLAINTEXT CONTENT:\n", plaintext_content, "\n")
    print("PARSED PLAINTEXT CONTENT:\n", parsed_plaintext_content, "\n")

    # Ngram creation will use list of list of words outputted from parsers
    # Ngram creation will also use metadata here in assembly of ngrams - no it won't?
    parsed_content = [["my", "amazing", "book"], ["hello", "world", "book"]]
    # main here will get stopwords so the list is identical across all
    # three sets of ngrams
    stopwords = ["my"]
    ngrams = {1 : ngram_creator.create(text, 1, stopwords, False),\
              2 : ngram_creator.create(text, 2, stopwords, True),\
              3 : ngram_creator.create(text, 3, stopwords, True)}


    # Packages up content from ngrams and metadata for output
    metadata_out = ({ "title" : "My Amazing Book", indices : [ 0 ] },\
                    { "author" : "Meg" })
    output = {}
    output["title"] = metadata_out[0]
    if len(metadata_out) > 1:
        output["metadata"] = metadata_out[2]
    output["ngrams"] = ngrams

    # Write to file as JSON
    fout = open("dummy.txt", "w")
    json.dump(output, fout)


if __name__ == "__main__":
    #main() for testing

    # Read in command line arguments
    if len(sys.argv) != 3:
        print("USAGE: python3 script filename file_type")
        sys.exit()

    filename = sys.argv[1]
    file_type = sys.argv[2]

    print("DEBUG:\tFilename:\t{}\n\tFile type:\t{}" \
        .format(filename, file_type) )

    # Open and read in file
    f = open(filename, "r")
    text = f.read()
    f.close()

    # eventual full output dictionary
    output = {}

    # it doesn't really make sense for the main code to deal with parser
    # objects - can we rework this slightly? especially since markdown
    # and plain text have only one function (parse) and aren't really
    # instantiated in any way that makes classes useful

    # we are using python 3, right? if so all print calls in Bs4Wrapper
    # are incorrect

    if file_type == "html":
        """
        html_parser = Bs4Wrapper.Bs4Wrapper(text)

        html_parser.clear_comments()
        text_lists = html_parser.extract_plain_text_lists():

        output["title"] = html_parser.get_title()
        output["metadata"] = html_parser.get_metadata()
        # del metadata if empty
        """
    else:
        # set title fields to empty
        output["title"] = { "title": "", "indices": [] }

    if file_type == "md":
        # markdown parser - needs to be fixed slightly
        # MDParser = md_parser.MarkdownParser()
        # text_lists = MDParser.parse(text)
        pass

    # I don't think markdown parsing output aligns with html parsing output
    # right now - both need to be identical to feed into plaintext parsing

    # parse plain text
    # PTParser = plaintext_parser.PlaintextParser()
    # parsed_plaintext_content = PTParser.parse(text_lists)

    parsed_content = [["my", "amazing", "book"], ["hello", "world", "book"]]
    # main here will get stopwords so the list is identical across all
    # three sets of ngrams

    # alternately, might make a driver class for n-gram creator that does
    # stopwords and the three separate calls so that implementation detail
    # isn't seen in main?
    stopwords = ["my"]
    ngrams = {1 : ngram_creator.create(text, 1, stopwords, False),\
              2 : ngram_creator.create(text, 2, stopwords, True),\
              3 : ngram_creator.create(text, 3, stopwords, True)}


    # Packages up content from ngrams and metadata for output
    if len(metadata_out) > 1:
        output["metadata"] = metadata_out[2]
    output["ngrams"] = ngrams

    # Write to file as JSON
    fout = open("dummy.txt", "w")
    json.dump(output, fout)
