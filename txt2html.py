#!/usr/bin/python
import sys


class Util:
    header = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>{title_name}</title>
    </head>
    """

    footer = """
</html>"""

    def print_header(self, name):
        print self.header.format(title_name=name.rstrip().strip())

    def print_footer(self):
        print self.footer


body = "<body><pre>\n"

line = sys.stdin.readline()
while line:
    body = body + line
    if line.startswith("NAME"):
        break
    else:
        line = sys.stdin.readline()

line = sys.stdin.readline()

util = Util()
util.print_header(line)

line = sys.stdin.readline()
while line:
    body = body + line
    line = sys.stdin.readline()

body = body + "    </pre></body>"
print body
util.print_footer()
