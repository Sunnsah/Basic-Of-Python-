# question number 8 to make copy of text file

with open("this.txt") as f:
    content = f.read()


    with open ("copy.this", "w") as f:
        f.write(content)