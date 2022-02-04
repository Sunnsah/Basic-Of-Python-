# question number three to replace the word from text file

wrongword = ["kala", "pala ", " sala"]
with open("sample.txt") as file:
    content = file.read()

    for word in wrongword:
        content = content.replace(wrongword, "#$^%#$^#")

with open("sample.txt", "w") as file:
    file.write(content)
