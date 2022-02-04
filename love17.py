#write a letter without changing data and name again and again

letter = '''Dear Sir, <|NAME|>
You got selected for Software developer job
  ***Congratulation to you and your family***
  Have a Great Day Sir
  <|DATE|>'''

name = input("Enter your name \n")
date = input ("Enter  Today Date \n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
