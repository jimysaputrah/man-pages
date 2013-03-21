#!/usr/bin/python
import os

inputdir = "html/osx10.8"
for root, _, files in os.walk(inputdir):
    for f in files:
        fullpath = os.path.join(root, f)
        basename = os.path.basename(fullpath)
        print "http://macmanpages.com/osx10.8/" + basename
