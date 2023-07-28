#!/usr/bin/python3

import os
import re

import sys
import time
import json

topdir = 'Copybooks'

outputdir = 'GradeScopeUploads'

try:
    os.mkdir(outputdir)
except FileExistsError as mkdirex:
    print('Directory {dd} already exists.'.format(dd=outputdir))

for dir1name in os.listdir(topdir):
    d1 = os.path.join(topdir, dir1name)
    if os.path.isdir(d1):
        for dir2name in os.listdir(d1):
            d2 = os.path.join(d1, dir2name)
            if os.path.isdir(d2):
                for fname in os.listdir(d2):
                    if fname == 'Color-orig.pdf':
                        oldname = os.path.join(d2, fname)
                        if os.path.isfile(oldname):
                            print(oldname)
                            newfname = 'Color.pdf'
                            newname = os.path.join(d2,newfname)
                            try:
                                os.rename(oldname, newname)
                            except:
                                print('Error doing rename from {oldname} to {newname}'.format(oldname=oldname,newname=newname))
            if not os.listdir(d2):
                try:
                    os.rmdir(d2)
                except:
                    print('Error doing rmdir to {d2}'.format(d2=d2))
        if not os.listdir(d1):
            try:
                os.rmdir(d1)
            except:
                print('Error doing rmdir to {d1}'.format(d1=d1))
