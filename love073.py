# problem no.6 to find the python in log file
content = True
i = 1

with open("log.file") as file:
    while content:
        content = file.readline()

        if 'python' in content.lower():
            print(content)
    print("Python is present ")
    print(i)
    i += 1


