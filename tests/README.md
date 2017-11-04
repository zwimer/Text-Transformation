The following test cases each assume the system is up and running, and that every other part is functioning correctly.

For the following test cases, assume the list of stop words contains the following:
1. megaphone
2. couch
3. design

For each test case, assume we are passed in a path to a file and a file type for that path. For all files in the HTML directory, assume the file type is '.html', for all files in the Markdown directory, assume the file type is '.md', and for all other files assume the file is a text file.

For HTML files, the following is assumed *not* to exist. If any of the following exists, it may cause improper results
1. Languages other than CSS, Javascript, or HTML
2. Comments in inlined or internal css
3. Raw strings
4. Escaped newlines trailing single line comments (i.e. on the same line)
5. Improperly formatted HTML
6. Nested HTML tags

For markdown files, the following is assumed *not* to exist. If any of the following exists, it may cause improper results
1. HTML in markdown

As for markdown, if links have a title defined with their definition, it is ignored.
