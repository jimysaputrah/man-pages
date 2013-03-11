#!/usr/bin/python
import sys

line = sys.stdin.readline()
while line:
    words = line.split()
    if len(words) > 0:
        man_page_name = words[0]
        link = "<a href=\"./osx10.8/" + man_page_name.replace("(", ".").replace(")", ".") + "html\">" + man_page_name + "</a>"
        print line.replace(man_page_name, link).rstrip()
    line = sys.stdin.readline()
