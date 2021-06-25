#!/usr/bin/env python3

import requests
import file
import os

'''To upload image file to endpoint URL'''
URL = "http://[IP-ADDRESS]/upload/"
DIR = "supplier-data/images/"

'''Get list of files in DIR'''
list = file.get_filelist(DIR)
for f in list:
    '''Split the filename from its extension'''
    file_tup = os.path.splitext(f)
    '''Get only jpeg files''' 
    if file_tup[1] == ".jpeg":
        with open(os.path.join(DIR,f), 'rb') as img:
            '''Post jpeg files to URL'''
            r = requests.post(URL, files={'file': img})
            
