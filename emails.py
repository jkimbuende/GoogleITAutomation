#!/usr/bin/env python3
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

message = EmailMessage()

def generate_email(sender, recipient, subject, body, attachment):
  message['From'] = sender
  message['To'] = recipient
  message["Subject"] = subject
  message.set_content(body)


  if not attachment_path == "":
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment, 'rb') as ap:
      message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment))


def send_email():
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
