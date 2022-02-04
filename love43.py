#Question number 7 of chapter 6 : check this post talking about David or not

text = input("Enter a name : ")

if("David" in text):
    # print("This  post talking about David")
    talk = True
elif("david" in text):
    talk = True
elif("DaviD" in text):
    talk = True
elif("DAvid" in text):
    talk = True      
else:
    talk = False

if(talk):
    print("this post is talking about David ")
else:
    print("This post is not talking about David")        

 