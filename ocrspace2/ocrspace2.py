# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:06:17 2019

@author:

This is example code to extract chinese subtitles from images
"""

import ocrspace
import time

# limit of 500 number of times within 86400
# api = ocrspace.API()
# Or if you have an API key or desired language, pass those:
# ocrspace.Language.Croatian

api = ocrspace.API('erasedApiKey', 'chs')
filelist = []
myString = ""
with open('file.txt', 'r') as f:
    for lin in f:
        filelist.append(lin.strip())

for imagefile in filelist:
    currentText = api.ocr_file(imagefile).rstrip().replace("\n","")
    # if image has two lines of text then join them as one
    currentText = " ".join(currentText.splitlines())
    # if unrecongizable text
    if currentText == "":
        currentText = 'no text here'
    time.sleep(4)
    with open("subtitle.txt", "a", encoding='utf-8') as resfile:
        resfile.write(currentText)
        resfile.write('\n')
    print(imagefile)
