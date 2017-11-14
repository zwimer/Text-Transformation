import plaintext_parser
import md_parser
import content_converter

# For testing
def main():
    # == PLAINTEXT ==
    plaintext_content = "This is from a plaintext file. For details, refer to the file.\n\nHello World, this is my file."
    parsed_plaintext_content = plaintext_parser.parse(plaintext_content)
    converted_plaintext_content = content_converter.convert(parsed_plaintext_content)
    # Here is where we would send the list of list of words to ngram creation

    # == MARKDOWN ==
    # TODO: make this actually markdown
    md_content = "This is markdown."
    parsed_md_content = md_parser.parse(md_content)
    converted_md_content = content_converter.convert(parsed_md_content)
    # Here is where we would send the list of list of words to ngram creation

if __name__ == "__main__":
    main()
