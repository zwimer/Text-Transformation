# System Integration Testing Notes

- All original output files were edited for correct JSON formatting.
- Additional resource if need be: http://www.jsondiff.com/

Tests that have failed and been documented have donotrun_ appended to the
function name so new tests are easier to see - remove that phrase to run all
tests, including previously failed ones

## Plaintext Tests

| Test | Outcome | Notes |
|------------------------|
| Casing | **PASS** |  |
| Punctuation | **PASS** |  |
| Stop Punctuation | **PASS** | Originally failed due to incorrect output file - indices for "is" onward on two- and three- grams were shifted one greater |
| Stop Words | **PASS** |  |
| Whitespace | **PASS** |  ||

## HTML Tests

| Test | Outcome | Notes |
|------------------------|
| Abbreviated Tags | PASS |  |
| Duplicate Metadata | PASS | Originally failed due to an index error in the expected output file |
| Duplicate Title | PASS | Originally failed due to capitalization error in expected output |
| General-1 | **FAIL** | Lines 2 and 3 are not registered as having anything that counts as a stopword between them. I believe the output file is in error here, but want to check before changing it. |
| General-2 | PASS | Originally failed due to error in output file (extraneous space in a term) |
| HTML in Javascript Comments | **FAIL** | HTML is Javascript Comments is not ignored; General-1 error |
| Inline CSS | PASS | Originally failed due to an index error in expected output - a word repeated in the input was only indexed once |
| Inline PHP | PASS |  |
| Internal CSS | PASS |  |
| Javascript Comments | PASS |  |
| Meta Title | PASS |  |
| Multi-line Comments | PASS |  |
| Nested HTML Comments | PASS |  |
| No Meta Tags | PASS |  |
| No Title | PASS |  |
| Plaintext | PASS | |
| Script tags | PASS |  |
| Single Line Comments | PASS |  |
| Special Characters | PASS |  |
| Tags | PASS |  |
| Title / Meta Title | PASS |  ||

## Markdown Tests

| Test | Outcome | Notes |
|------------------------|
| General-1 | **FAIL** |Originally failed due to the output file being the output for a separate test; Likely failing due to incorrect output file, not system failure |
| Inline Image | PASS |  |
| Inline Image with Extra | **NOT RUN** |  |
| Inline Link Style | **PASS** |  |
| Inline Link Style with Extra | **NOT RUN** |  |
| Multi-tick Code Blocks | **NOT RUN** |  |
| Numbered Reference Style Link | **NOT RUN** |  |
| Reference Image | **NOT RUN** |  |
| Reference Image with Extra | **NOT RUN** |  |
| Reference Style Link | **NOT RUN** |  |
| Relative Repository Reference Link | **NOT RUN** |  |
| Self Reference Style Link | **NOT RUN** |  |
| Single Tick Code Blocks | **NOT RUN** |  ||

## Other Tests

- Binary File: That output does not seem to align with our specs. Binary files should not produce any output at all - currently, the system will error on any file that is not within the expected types.
