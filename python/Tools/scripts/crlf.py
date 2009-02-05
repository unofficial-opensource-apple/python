#! /usr/bin/env python

"Replace CRLF with LF in argument files.  Print names of changed files."

import sys, os
for file in sys.argv[1:]:
    if os.path.isdir(file):
        print file, "Directory!"
        continue
    data = open(file, "rb").read()
    if '\0' in data:
        print file, "Binary!"
        continue
    newdata = data.replace("\r\n", "\n")
    if newdata != data:
        print file
        f = open(file, "wb")
        f.write(newdata)
        f.close()
