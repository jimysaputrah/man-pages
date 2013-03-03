#!/usr/bin/python
import os
from subprocess import call

path = "/usr/share/man/"
outputdir = "txt/osx10.8"
for root, _, files in os.walk(path):
    for f in files:
        fullpath = os.path.join(root, f)
        basename = os.path.basename(fullpath)
        if basename != "whatis":
            call("man " + fullpath + " |col -b >" + outputdir + "/" + basename + ".txt", shell=True)
        #print fullpath
