import string
import re

# Input: String
# Output: list of list of strings (lower cased individual words)
def parse(content):

    print("this is original:\n", content)

    translator = str.maketrans('', '', string.punctuation)
    parsed = content.translate(translator)
    parsed = parsed.lower()

    # First, need to split on escape characters
    # (except html tags; this is done by HTML parser)
    word_list = re.split('\n\t|\n\n|\n\#', parsed)

    # Second, need to split on whitespace to break up words

    print("this is word list:\n", word_list)

    return parsed
