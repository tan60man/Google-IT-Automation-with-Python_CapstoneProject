#!/usr/bin/env python3

import psutil
import shutil
import socket
import sys

def health_criteria():
    good_health = True
    errors = []
    if psutil.cpu_percent(1) > 80:
        good_health = False
        errors.append("Error - CPU usage is over 80% with usage at {}".format(psutil.cpu_percent(1)))
    if psutil.virtual_memory().available > 500*1024^2:
        good_health = False
        errors.append("Error - Available memory is less than 500MB with available memory at {}".format(psutil.virtual_memory()))
    if shutil.disk_usage("/mnt/c/Users/65965/")[2]/ shutil.disk_usage("/mnt/c/Users/65965/")[0] < 0.2:
        good_health = False
        errors.append("Error - Available disk space is less than 20% with available disk space at {}".format(shutil.disk_usage("/mnt/c/Users/65965/")[2]))
    if socket.gethostbyname("localhost") != "127.0.0.1":
        good_health = False
        errors.append("Error - localhost cannot be resolved to 127.0.0.1")
        
    return good_health , errors
    
def main(argv):
    print(health_criteria())
    good_health, errors = health_criteria()
    if not good_health:
        for error in errors:
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            subject = error
            body = "Please check your system and resolve the issue as soon as possible."
            message = emails.generate_without_attachment(sender, receiver, subject, body)
            emails.send(message)
            
if __name__ == "__main__":
    main(sys.argv)
