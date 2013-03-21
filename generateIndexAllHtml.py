#!/usr/bin/python
import os


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


inputdir = "html/osx10.8"
for root, _, files in os.walk(inputdir):
    for f in files:
        fullpath = os.path.join(root, f)
        basename = os.path.basename(fullpath)
        print "<a href=\"osx10.8/" + basename + "\">" + rreplace(basename[:-5], ".", "(", 1) + ")" + "</a>"
