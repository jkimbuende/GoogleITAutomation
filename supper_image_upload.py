#!/usr/bin/env python3
import requests
import os
# This python script will upload the .jpeg files
# to the web server

url = "http://localhost/upload/"

os.chdir("./supplier-data/images")

for file in os.listdir("."):
  if ".jpeg" in file:
    print(file)
    with open(file, "rb") as opened:
      r = requests.post(url, files={'file': opened})
