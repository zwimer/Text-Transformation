# NGram Creation
# Author: Lee Cattarin
# Date created: 15 Nov 2017
# Date last edited: 16 Nov 2017


def sanitize_stopwords(stopwords):
    """
    :param stopwords: list of stopwords
    :returns None
    Edits the stopword list in place to ensure words are stripped of
        spaces and lowercase
    """
    for i, word in enumerate(stopwords):
        stopwords[i] = word.strip().lower()


def create(text, number_of_terms, stopwords, use_stopwords):
    """
    :param text: list of lists of sanitized strings
    :param number_of_terms: desired ngram length
    :param stopwords: list of stopwords
    :use_stopwords: True if stopwords are taken into account,
        False if they are treated as normal words
    :returns dictionary of key, value = term, [indices]
    Creates a dictionary of terms of the given length and their indices
        in the text body
    """
    terms = {}
    index = 0  # index in full text

    # Current term details
    # (term, term length)
    current_term = []
    current_length = 0

    # Terminology:
    # Text: full list of lists
    # Section: one list in text (considered delimited at beginning and end)
    # Word: single string in section

    for section in text:

        # Skip sections that do not have enough words to create a term
        if len(section) < number_of_terms:
            index += len(section)
            continue

        # Reset the current term details
        current_term = []
        current_length = 0

        for word in section:
            index += 1

            # Reset the term details when a stopword is encountered
            # (if stopwords are being used)
            if word in stopwords and use_stopwords:
                current_term = []
                current_length = 0
                continue

            # Otherwise, add to the term
            current_term.append(word)
            current_length += 1

            # If the term is long enough, add it
            if current_length == number_of_terms:
                new_term = " ".join(current_term)

                if new_term not in terms:
                    terms[new_term] = []
                terms[new_term].append(index - number_of_terms)

                current_term = current_term[1:]
                current_length -= 1

    return terms

# All below this only for test use


def test(text, stopwords):
    """
    :param text: text as a list of lists of words
    :param stopwords: the list of stopwords
    :returns None
    Runs a single test with the given text and stopwords
    """
    print("=" * 72)
    print("Test:\nstarting text: {}\nstopwords: {}\n".format(text, stopwords))

    ngrams = {1: create(text, 1, stopwords, False),
              2: create(text, 2, stopwords, True),
              3: create(text, 3, stopwords, True)}

    for key, value in ngrams.items():
        print("Ngram length: {}".format(key))
        for term, indices in value.items():
            print("\t{}: {}".format(term, indices))

    print("=" * 72, "\n")


def main():
    text = [["my", "amazing", "book"], ["hello", "world", "book"]]
    stopwords = ["my"]
    # sanitize_stopwords(stopwords)
    test(text, stopwords)

    text = [["this", "is", "a", "sentence", "with", "lots", "of",
             "stopwords"], ["short"], ["long", "sentence", "here",
                                       "and", "repetition", "of",
                                       "sentence", "stopwords"]]
    stopwords = ["this", "is", "a", "with", "of", "and"]
    sanitize_stopwords(stopwords)
    test(text, stopwords)

    # more tests here


if __name__ == "__main__":
    main()
