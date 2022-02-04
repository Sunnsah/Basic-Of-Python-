# Question set of chapter 9 first question to make a file and found twinkle is present or not !

file = open ("poem.txt")
time = file.read()
if 'Blueeye' in time:
    print("blue eye is present in this poem ")

else :

    print("eye is not present in this peom")    
file.close()