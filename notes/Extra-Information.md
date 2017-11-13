Stop 'punctuation' are defined as follows:

1. All html tags
2. \n\t
3. \n\n
4. \n#
5. \n>

For HTML files, the following is assumed *not* to exist. If any of the following exists, it may cause improper results

1. Languages other than CSS, Javascript, or HTML
2. Comments in inlined or internal css
3. Raw strings
4. Escaped newlines trailing single line comments (i.e. on the same line)
5. Improperly formatted HTML
6. Nested HTML tags
7. Not all metadata and title tags desired are parsed by Beautiful Soup perfectly, and no others     are. (Ie, corner cases not handled by Beautiful Soup are not handled by this program)

For markdown files, the following is assumed **not** to exist. If any of the following exists, it may cause improper results

1. HTML in markdown

As for markdown, if links have a title defined with their definition, it is ignored. Finally, if ever anything should be ignored, as far as 'to be ignored items' go, it should be treated as if the  to be ignored text was replaced with a single space. For example:
```
Hello<script>

</script>World
```
Will become
```
Hello World
```

That being said, this also implies that
```
Hello
<script>
</script>
World
```
Will become
```
Hello

World
```
