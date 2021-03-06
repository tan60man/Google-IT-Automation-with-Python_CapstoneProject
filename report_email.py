#!/usr/bin/env python3

import os
import datetime
import reports
import emails
import run
import sys

'''To generate pdf report from data in DIR and send emails'''
DIR = "supplier-data/descriptions/"

def process_data(data):
    report_data = []
    for item in data:
        content = ["name: {}\nweight: {} lbs".format(item["name"],item["weight"])]
        report_data.append(content)
    return report_data
    
def main(argv):
    data = process_data(run.dict_files(DIR))
    reports.generate("/tmp/processed.pdf", "Processed Update on {}". format(datetime.datetime.now().strftime("%B %d, %Y")), data)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)
    
if __name__ == "__main__":
    main(sys.argv)
    
