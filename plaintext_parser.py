import string

def parse(content):

    print("this is original:\n", content)

    translator = str.maketrans('', '', string.punctuation)
    parsed = content.translate(translator)

    print("this is parsed:\n", parsed)

    return parsed
