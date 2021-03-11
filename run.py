#! /usr/bin/env python3
import os
import requests

os.chdir("./supplier-data/descriptions")

for file in os.listdir("."):
    dict = {}
    name = ""
    weight = ""
    description = ""
    image_name = ""
    with open(file, "r") as f:
        name = f.readline().strip()
        weight = f.readline().strip()
        description = f.readline().strip()

    weight = int( weight.replace(" lbs", "") )

    dict["name"] = name
    dict["weight"] = weight
    dict["description"] = description
    dict["image_name"] = file.replace(".txt", ".jpeg")
    print(dict)

    # TODO: Change IP Address
    rp = requests.post("http://35.202.122.98/fruits/", json=dict)
