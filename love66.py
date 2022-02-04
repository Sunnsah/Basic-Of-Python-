# use of strip function

def remove_and_strip(string , word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    David is Smart guys    "
b = remove_and_strip(this, "David")
# print(this)
# print(this.strip())
print(b)