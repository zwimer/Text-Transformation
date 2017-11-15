import plaintext_parser
import md_parser

# For preliminary testing
def main():
    # Raw input comes into text_transformation

    # If input is html, call html_parser here

    # If input is markdown, call md_parser here
    # TODO: make this actually markdown
    md_content = "# This is a \n\n general Markdown test\n\n```c++\nAnd boy is it ever\n#magic!\n```"
    parsed_md_content = md_parser.parse(md_content)

    # If input is just plaintext:
    plaintext_content = "Break here\n\n. Again, #break here;\n\tHello World!\nBREAK HERE \n\# . Don't avoid\n>contractions."
    parsed_plaintext_content = plaintext_parser.parse(plaintext_content)

    # Ngram creation will use list of list of words outputted from parsers
    # Ngram creation will also use metadata here in assembly of ngrams

if __name__ == "__main__":
    main()
