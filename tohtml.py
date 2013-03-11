#!/usr/bin/python
import os
from subprocess import call

inputdir = "txt/osx10.8"
outputdir = "html/osx10.8"
for root, _, files in os.walk(inputdir):
    for f in files:
        fullpath = os.path.join(root, f)
        basename = os.path.basename(fullpath)
        if basename != "whatis":
            print "Processing: " + basename
            new_basename = basename[:-4] + ".html"
            call("cat " + fullpath + " |./txt2html.py >" + outputdir + "/" + new_basename, shell=True)
        #print fullpath
