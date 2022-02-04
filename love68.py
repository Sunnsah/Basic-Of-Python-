# use of open ( ) function and close function
f = open('sample.txt', 'r')
data = f.read()
print(data)
f.close()