# System Integration Testing Notes

All original output files were edited for correct JSON formatting.

Additional resource if need be: http://www.jsondiff.com/

## Plaintext Tests

1. Casing: **PASS**
2. Punctuation: **PASS**
3. Stop Punctuation: **PASS**
  - Originally failed due to incorrect output file: indices for "is"
    onward on two- and three- grams were shifted one greater
4. Stop Words: **PASS**
5. Whitespace: **PASS**

## HTML Tests

1. General-1: **FAIL**
  - Lines 2 and 3 are not registered as having anything that counts as a
    stopword between them. I believe the output file is in error here, but
    want to check before changing it.
2. General-2: **PASS**
  - Originally failed due to error in output file (extraneous space in a
    term)
3. Interal CSS: **FAIL**
  - Same reason as General-1
4. Plaintext: **PASS**
5. Script tags: **FAIL**
  - Same reason as General-1

## Markdown Tests

1. General-1: **FAIL**
  - Originally failed due to the output file being the output for a
    separate test
  - Output file has been revised, but I believe it is wrong thanks to my
    knowledge of markdown - I'll check in class
2. Inline Image: **PASS**
3. Inline Link Style: **PASS**

## Other Tests

1. Binary File: That output does not seem to align with our specs. Binary files
  should not produce any output at all - currently, the system will error on
  any file that is not within the expected types.
