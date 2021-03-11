#!/usr/bin/env python3
import os
from datetime import date
import reports
import emails

os.chdir("./supplier-data/descriptions")

name_list = []
wt = []

for file in os.listdir("."):
    name = ""
    weight = ""
    with open(file, "r") as f:
        name = f.readline().strip()
        weight = f.readline().strip()
    name_list.append('name: ' + name)
    wt.append('weight: ' + weight)

    new_obj = ""

    for i in range( len(name_list) ):
        new_obj += name_list[i] + '<br />' + wt[i] + '<br />' + '<br />'

if __name__ == "__main__":
    user = os.getenv('USER')
    today = date.today()
    d = today.strftime("%B %d, %Y")
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on " + d
    paragraph = new_obj

    # Print statements for debugging
    # prints the path to the PDF, the title of the PDF, and the data
    print(attachment)
    print(title)
    print(paragraph)

    reports.generate_report(attachment, title, paragraph)
    subject = """Upload Completed - Online Fruit Store"""
    body = """All fruits are uploaded to our website successfully. A detailed list is attached to this email."""
    emails.generate_email("automation@example.com", user+"@example.com", subject, body, attachment)
    emails.send_email()
