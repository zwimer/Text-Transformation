# System Integration Testing Notes

- All original output files were edited for correct JSON formatting.
- Additional resource if need be: http://www.jsondiff.com/

## System Tests
(All are expected to error, exit, and create no output)

| Test | Outcome | Notes |
|------------------------|
| Binary File |

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
| General-1 | PASS | Originally failed due to the output file being the output for a separate test; Originally failed due to incorrect output file - '\n\t' not used as stopword |
| Inline Image | PASS |  |
| Inline Image with Extra | PASS |  |
| Inline Link Style | PASS |  |
| Inline Link Style with Extra | PASS |  |
| Multi-tick Code Blocks | PASS |  |
| Numbered Reference Style Link | PASS |  |
| Reference Image | PASS |  |
| Reference Image with Extra | PASS |  |
| Reference Style Link | PASS |  |
| Relative Repository Reference Link | PASS |  |
| Self Reference Style Link | PASS |  |
| Single Tick Code Blocks | PASS |  ||
