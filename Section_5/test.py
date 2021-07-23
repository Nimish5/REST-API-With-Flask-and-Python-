# find list of images in a nested directory(jpg, jpeg, png)
# input = Images
# output = List of images with its full path

import os
arr = []
for r, d, f in os.walk(r"C:\Users\User\.vscode\Section5 (Virtualenv)\code\Images"):
    for file in f:
        arr.append(os.path.join(r, file))

for f in arr:
    print(f)



