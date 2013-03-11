#!/usr/bin/python
import sys


class Util:

    header = """<!DOCTYPE html>
<html>
    <head>
        <meta name="description" content="{description}..." />
        <meta http-equiv="Content-Type" CONTENT="text/html; charset="utf-8" />
        <script type="text/javascript" src="../js/ga.js"></script>
        <title>{title_name}</title>
        <META NAME="robots" CONTENT="all" />
    </head>
    """

    footer = """
</html>"""

    def print_header(self, name, desc):
        print self.header.format(title_name=name.rstrip().strip(), description=desc.rstrip().strip())

    def print_footer(self):
        print self.footer


content = "\n"

line = sys.stdin.readline()
while line:
    content = content + line
    if line.lower().startswith("name"):
        break
    else:
        line = sys.stdin.readline()

name = sys.stdin.readline()
content = content + name


line = sys.stdin.readline()
while line:
    content = content + line
    if line.lower().startswith("description"):
        break
    else:
        line = sys.stdin.readline()

desc = sys.stdin.readline()
content = content + desc


util = Util()
util.print_header(name, desc)

line = sys.stdin.readline()
while line:
    content = content + line
    line = sys.stdin.readline()

content = content.replace("<", "&lt").replace(">", "&gt")

body = "<body><pre>\n" + content + "    </pre></body>"
print body
util.print_footer()
