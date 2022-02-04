# problem no.6 to find the python in log file


with open("log.file") as file:
    content = file.read()

if 'python' in content.lower():
    print("python is present in log ")
else:
    print("no python is not present ")
