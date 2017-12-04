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

| Test | Outcome | Notes |
|------------------------|
| Abbreviated Tags | **FAIL** | General-1 error |
| Duplicate Metadata | **FAIL** | General-1 error; Originally additionally failed due to an index error in the expected output file |
| Duplicate Title | **FAIL** | General-1 error; Originally additionally failed due to capitalization error in expected output |
| General-1 | **FAIL** | Lines 2 and 3 are not registered as having anything that counts as a stopword between them. I believe the output file is in error here, but want to check before changing it. |
| General-2 | **PASS** | Originally failed due to error in output file (extraneous space in a term) |
| HTML in Javascript Comments | **FAIL** | HTML is Javascript Comments is not ignored; General-1 error |
| Inline CSS | **FAIL** | General-1 error; Originally additionally failed to an index error in expected output - a word repeated in the input was only indexed once |
| Inline PHP | **FAIL** | General-1 error |
| Internal CSS | **FAIL** | General-1 error |
| Javascript Comments | **FAIL** | General-1 error |
| Meta Title | **FAIL** | General-1 error |
| Multi-line Comments | **FAIL** | General-1 error |
| Nested HTML Comments | **FAIL** | General-1 error |
| No Meta Tags | **PASS** |  |
| No Title | **FAIL** | General-1 error |
| Plaintext | **PASS** | |
| Script tags | **FAIL** | General-1 error |
| Single Line Comments | **NOT RUN** |  |
| Special Characters | **NOT RUN** |  |
| Tags | **NOT RUN** |  |
| Title / Meta Title | **NOT RUN** |  ||

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
