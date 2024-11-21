# Exercise 7 Solution   Shoutouts

import os

files = os.listdir("Folder Name")
i = 1
for file in files:
    if file.endwith(".png"):  # PNG or any extension
        print(files)
        os.rename(f"FolderName/(file)", f"FolderName/{i}.png")
