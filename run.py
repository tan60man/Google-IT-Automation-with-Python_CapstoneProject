#!/usr/bin/env python3

import os
import requests
import file

'''To process text files in DIR to stipulatd format and post it to URL''' 
URL = "http://[IP-ADDRESS]/fruits/?format=api"
DIR = "supplier-data/descriptions/"

'''Extract content from files in dir and pass it to a list of dictionaries with keys (name,weight,description and image_name)'''
def dict_files(dir):
    list_dict = []
    filecontent = {}
    '''Get list of files in dir'''
    files = file.get_filelist(dir)
    for f in files:
        with open(os.path.join(dir,f), 'r') as content:
            '''Extract individual line'''
            lines = content.readlines()
            '''Remove lbs in weight'''
            weight = int(lines[1].replace(" lbs",""))
            '''Change file name's extension from "txt" to "jpeg" as corresponding image shares the same name as the txt file in jpeg format'''
            image_name = f.replace("txt", "jpeg")
            filecontent["name"] = lines[0]
            filecontent["weight"] = weight
            filecontent["description"] = lines[2]
            filecontent["image_name"] = image_name
            content.close()
        return list_dict

'''Post data to URL'''
def post_description(url,data):
    r =requests.post(url,data)
    '''Ensure that it returns status code 2xx'''
    return r.status_code 
    
if __name__ == "__main__":
    for data in dict_files(DIR):
        print(post_description(URL,data))
