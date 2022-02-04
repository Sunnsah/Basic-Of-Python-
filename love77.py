# How to rename the file Name

import os
oldname = "this.txt"
newname = "new_file_name.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
     f.write(content)

os.remove(oldname)