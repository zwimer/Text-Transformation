# System Integration Testing Notes

- All original output files were edited for correct JSON formatting.
- Additional resource if need be: http://www.jsondiff.com/

Tests that have failed and been documented have donotrun_ appended to the
function name so new tests are easier to see - remove that phrase to run all
tests, including previously failed ones

## Plaintext Tests

1. Casing: **PASS**
2. Punctuation: **PASS**
3. Stop Punctuation: **PASS**
  - Originally failed due to incorrect output file: indices for "is"
    onward on two- and three- grams were shifted one greater
4. Stop Words: **PASS**
5. Whitespace: **PASS**

## HTML Tests

1. Abbreviated Tags: **FAIL**
  - Same reason as General-1
2. Duplicate Metadata: **FAIL**
  - Same reason as General-1
  - Originally additionally failed due to an index error in the expected output
    file
3. Duplicate Title: **FAIL**
  - Same reason as General-1
  - Originally additionally failed due to capitalization error in expected
    output
4. General-1: **FAIL**
  - Lines 2 and 3 are not registered as having anything that counts as a
    stopword between them. I believe the output file is in error here, but
    want to check before changing it.
5. General-2: **PASS**
  - Originally failed due to error in output file (extraneous space in a
    term)
6. HTML in Javascript Comments: **FAIL**
  - HTML is Javascript Comments is not ignored
  - Error from General-1 is also present
7. Inline CSS: **FAIL**
  - Same reason as General-1
  - Originally additionally failed to an index error in expected output - a word
    repeated in the input was only indexed once
8. Inline PHP: **FAIL**
  - Same reason as General-1
9. Internal CSS: **FAIL**
  - Same reason as General-1
10. Javascript Comments: **NOT RUN**
11. Meta Title: **NOT RUN**
12. Multi-line Comments: **NOT RUN**
13. Nested HTML Comments: **NOT RUN**
14. No Meta Tags: **NOT RUN**
15. No Title: **NOT RUN**
16. Plaintext: **PASS**
17. Script tags: **FAIL**
  - Same reason as General-1
18. Single Line Comments: **NOT RUN**
19. Special Characters: **NOT RUN**
20. Tags: **NOT RUN**
21. Title / Meta Title: **NOT RUN**

## Markdown Tests

1. General-1: **FAIL**
  - Originally failed due to the output file being the output for a
    separate test
  - Output file has been revised, but I believe it is wrong thanks to my
    knowledge of markdown - I'll check in class
2. Inline Image: **PASS**
3. Inline Image with Extra: **NOT RUN**
4. Inline Link Style: **PASS**
5. Inline Link Style with Extra: **NOT RUN**
6. Multi-tick Code Blocks: **NOT RUN**
7. Numbered Reference Style Link: **NOT RUN**
8. Reference Image: **NOT RUN**
9. Reference Image with Extra: **NOT RUN**
10. Reference Style Link: **NOT RUN**
11. Relative Repository Reference Link: **NOT RUN**
12. Self Reference Style Link: **NOT RUN**
13. Single Tick Code Blocks: **NOT RUN**

## Other Tests

1. Binary File: That output does not seem to align with our specs. Binary files
  should not produce any output at all - currently, the system will error on
  any file that is not within the expected types.
