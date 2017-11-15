import string
import re

# Input: String
# Output: list of list of strings (lower cased individual words)
# TODO: Need to fix contractions i.e. don't, won't, etc.
def parse(content):

    print("this is original:\n", content)

    # Lower case all words
    content = content.lower()

    # Remove all symbols except # and > (for use with stop punctuation later)
    punct = re.sub("[#>]", "", string.punctuation)
    translator = str.maketrans("", "", punct)
    parsed = content.translate(translator)

    # First, need to split on escape characters
    # (except html tags; this is done by HTML parser)
    word_list = re.split("\n\t|\n\n|\n\#|\n>", parsed)

    # Second, need to remove extraneous # and >
    # that were not part of stop punctuation
    new_word_list = []
    for word in word_list:
        translator = str.maketrans("", "", "#>")
        new_word_list.append( word.translate(translator) )

    # Finally, split on whitespace to get individual words
    list_of_lists = []
    for word in new_word_list:
        section = word.split()
        list_of_lists.append( section )

    print("this is list of list of words:\n", list_of_lists)

    return list_of_lists
