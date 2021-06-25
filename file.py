#!/usr/bin/env python3

import os

'''To get list of files in directory dir'''
def get_filelist(dir):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,file)): 
            files.append(file)
        return files
