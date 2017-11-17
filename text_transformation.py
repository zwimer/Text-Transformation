import plaintext_parser
import md_parser
import ngram_creator

# For preliminary testing
def main():
    # Raw input comes into text_transformation


    # If input is html, call html_parser here


    # If input is markdown, call md_parser here
    md_content = "# This is a \n\n general Markdown test\n\n```c++\nAnd boy is it ever\n#magic!\n```"
    parsed_md_content = md_parser.parse(md_content)

    # If input is just plaintext:
    plaintext_content = "Break here\n\n. Again, #break-here;\n\tHello World!\nBREAK- HERE \n\# . Don't avoid\n>contractions. James' lol"
    PTParser = plaintext_parser.PlaintextParser()
    parsed_plaintext_content = PTParser.parse(plaintext_content)

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
    main()
