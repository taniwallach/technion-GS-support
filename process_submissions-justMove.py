#!/usr/bin/python3

# The majority of the code from the long comment below and down is
# a modified version of repl-font.py from the PyMuPDF-Utilities repository,
# and the copyright of that code is as explained in that repository.
# Several of the import statements below were takes from repl-font.py
# and moved to the start of the file.

# Code not derived from PyMuPDF-Utilities is (c) 2023, Nathan Wallach

# Since this script is a derivative work based on code from
#     https://github.com/pymupdf/PyMuPDF-Utilities/
# it is also licensed under the AGPL-3.0 license.

import os
import zipfile
import re
import yaml

import sys
import time
import json
from pprint import pprint

# We use https://github.com/MeirKriheli/python-bidi
# which is licensed under LGPL3.0
from bidi.algorithm import get_display

import fitz

# Future work - get the exam code from a GUI or from the command line

examCode = '202202-104002-1'

# The locations of the font files being used for the replacements are
# correct for Ubuntu 22.04.

fontReplacements = {
        'NotoSans-Bold':    'D:\tani\LiberationFonts\LiberationSans-Bold.ttf',
        'NotoSans-Italic':  'D:\tani\LiberationFonts\LiberationSans-Italic.ttf',
        'NotoSans-Regular': 'D:\tani\LiberationFonts\LiberationSans-Regular.ttf'
        }

try:
    os.mkdir('Copybooks')
except FileExistsError as mkdirex:
    print('Copybooks directory already exists.')

# Extract and find submission_metadata.yml
with zipfile.ZipFile('submissions.zip', 'r') as zip:
    zip.extractall('./')
    inZip = zip.namelist()
    for item in inZip:
        if re.search("submission_metadata.yml", item):
            submission_metadata = item
            dirname, fname = os.path.split(item)
    print(submission_metadata)
    #print(dirname)

with open(submission_metadata, 'r', encoding='utf-8') as stream:
    try:
        submissions = yaml.safe_load(stream)
        print(submissions)
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)

pdffiles = list()

for item in submissions.keys():
    sid = submissions.get(item).get(':submitters')[0].get(':sid')

    print("sid found {sid}\n\n".format(sid = sid))
    d1 = os.path.join('Copybooks',sid)
    d2 = os.path.join(d1,examCode)
    oldname = os.path.join(dirname,item)
    newname = os.path.join(d2,'Color.pdf')
    for dd in [ d1, d2 ]:
        try:
            os.mkdir(dd)
        except FileExistsError as mkdirex:
            print('Directory {dd} already exists.'.format(dd=dd))
    try:
        os.rename(oldname, newname)
        pdffiles.append(newname)
    except:
        print('Error doing rename from {oldname} to {newname}'.format(oldname=oldname,newname=newname))

