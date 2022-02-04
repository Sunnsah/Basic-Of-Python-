#program to ask user not enter a spam comment : spam detactor


#Question number 7 of chapter 6 : check this post talking about David or not

text = input("Enter a Comment  : ")

if("make a lot of money" in text):
    spam = True
elif("like this" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("Subscribe" in text):
    spam = True      
else:
    spam = False

if(spam):
    print("This is spam comment ")
else:
    print("This is Not spam comment ")
            

 