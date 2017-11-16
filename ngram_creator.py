

# Check that stopwords are lowercase and stripped. Likely will not
# be necessary
def sanitize_stopwords(stopwords):
    for i, word in enumerate(stopwords):
        stopwords[i] = word.strip().lower()

# Expected input format:
# text: list of lists of sanitized strings
# number_of_terms: 1, 2, or 3 depending on the desired term length
# stopwords: list of string stop words obtained from indexing
def create(text, number_of_terms, stopwords, use_stopwords):
    terms = {}
    index = 0

    current = ("", 0) # current term and the number of words in it

    for section in text:
        if len(section) < number_of_terms:
            index += len(section)
            continue

        current = ("", 0) # current term and the number of words in it

        for word in section:
            index += 1

            if word in stopwords and use_stopwords:
                current = ("", 0)
                continue

            current = (current[0] + " " + word, current[1] + 1)

            if current[1] == number_of_terms:

                if not current[0] in terms:
                    terms[current[0]] = []
                terms[current[0]].append(index - number_of_terms)

                current = ("", 0)

    return terms

def test(text, stopwords):
    print("="*72)
    print("Test:\nstarting text: {}\nstopwords: {}\n".format(text, stopwords))

    ngrams = {1 : create(text, 1, stopwords, False),\
              2 : create(text, 2, stopwords, True),\
              3 : create(text, 3, stopwords, True)}

    for key, value in ngrams.items():
        print("Ngram length: {}".format(key))
        for term, indices in value.items():
            print("\t{}: {}".format(term, indices))

    print("="*72, "\n")

def main():
    text = [["my", "amazing", "book"], ["hello", "world", "book"]]
    stopwords = ["my"]
    #sanitize_stopwords(stopwords)
    test(text, stopwords)

    text = [["this", "is", "a", "sentence", "with", "lots", "of",\
            "stopwords"], ["short"], ["long", "sentence", "here",\
            "and", "repetition", "of", "sentence", "stopwords"]]
    stopwords = ["this", "is", "a", "with", "of", "and"]
    sanitize_stopwords(stopwords)
    test(text, stopwords)

    # more tests here

if __name__ == "__main__":
    main()
