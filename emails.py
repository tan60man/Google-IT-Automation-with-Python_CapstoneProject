#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib


'''To generate mail message and send message'''
def generate(sender, receipient, subject, body, attachment_path):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receipient
    message["Subject"] = subject
    message.set_content(body)
    
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=attachment_filename
                                
    return message
    
def generate_without_attachment(sender, receipient, subject, body, attachment_path):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receipient
    message["Subject"] = subject
    message.set_content(body)
    
    return message
    
def send(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit
    