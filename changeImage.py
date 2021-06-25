#!/usr/bin/env python3

from PIL import Image
import os
import file

'''To change the image file in directory "DIR" from a tiff format to a jpeg format and resize it to 600x400'''
DIR = "supplier-data/images/"

'''Convert the image to jpeg format and resize it to 600x400'''
def convert(img):
    im = img.convert("RGB").resize((600,400))
    return im
    
'''New file name to be saved in directory dir with .jpeg extension'''   
def get_savedname(dir,file):
    chngExt = file.replace("tiff", "jpeg")
    savedname = os.path.join(dir,chngExt)
    return savedname

if __name__ == "__main__":
    for f in file.get_filelist(DIR):
        '''To separate the file name and its extension'''
        split_tup = os.path.splitext(f)
        print(split_tup) 
        '''To get file name with .tiff extension and do conversion and save it with .jpeg extension'''
        if split_tup[1] == ".tiff":
            im = Image.open(os.path.join(DIR,f))
            savedname = get_savedname(DIR,f)
            convert(im).save(savedname)
            print("saved {}".format(savedname))
        
       
