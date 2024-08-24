# LNK-parse
A small CLI tool for parsing the metadata from .lnk files

The tool currently takes a single .lnk file's local path as input

It's currently only capable of parsing the header size, link flags,
link attributes, and the creation/access/write times

For testing I used a .lnk for Internet Explorer I got from a windows VM.
To actually test that the results were correct, I manually calculated
what the values of everything should be based of the hexdump output
of its bytes.
