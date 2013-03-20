#!/usr/bin/python
import os
from subprocess import call

path = "/usr/share/man/"
outputdir = "html/osx10.8"
for root, _, files in os.walk(path):
    for f in files:
        fullpath = os.path.join(root, f)
        basename = os.path.basename(fullpath)
        if basename != "whatis":
            print "Processing: " + basename
            new_basename = basename.replace(".gz", "") + ".html"
            call("man " + fullpath + " |./man2html >" + outputdir + "/" + new_basename, shell=True)
        #print fullpath
