# problem number 9 to check whether program is identical or duplicate

file1 = "this.txt"
file2 = "copy.txt"


with open (file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()


if f1==f2:
    print(f"this is identical or match with ")
else:
    print(f"this is NOt !! identical or match with ")

