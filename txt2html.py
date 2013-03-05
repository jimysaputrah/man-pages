#!/usr/bin/python
import sys


class Util:

    header = """<!DOCTYPE html>
<html>
    <head>
        <meta name="description" content="{description}..." />
        <meta http-equiv="Content-Type" CONTENT="text/html; charset="utf-8" />
        <title>{title_name}</title>
        <META NAME="robots" CONTENT="all" />
    </head>
    """

    footer = """
</html>"""

    google_analytics_js = """<script type="text/javascript" src="../js/ga.js"></script>"""

    def print_header(self, name, desc):
        print self.header.format(title_name=name.rstrip().strip(), description=desc.rstrip().strip())

    def print_footer(self):
        print self.footer


body = "<body><pre>\n"

line = sys.stdin.readline()
while line:
    body = body + line
    if line.lower().startswith("name"):
        break
    else:
        line = sys.stdin.readline()

name = sys.stdin.readline()
body = body + name


line = sys.stdin.readline()
while line:
    body = body + line
    if line.lower().startswith("description"):
        break
    else:
        line = sys.stdin.readline()

desc = sys.stdin.readline()
body = body + desc


util = Util()
util.print_header(name, desc)

line = sys.stdin.readline()
while line:
    body = body + line
    line = sys.stdin.readline()

body = body + "    </pre>" + util.google_analytics_js + "</body>"
print body
util.print_footer()
