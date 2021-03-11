#!/usr/bin/env python3
import os
from PIL import Image
import shutil

os.chdir("./supplier-data/images")

for file in os.listdir("."):
    filename = os.fsdecode(file)
    if (filename == "LICENSE") or (filename == "README"):
        continue
    print(filename)
    im = Image.open(filename).convert("RGB")
    temp_im = im.resize((600,400))
    new_filename = filename.replace("tiff", "jpeg")
    temp_im.save(new_filename)
