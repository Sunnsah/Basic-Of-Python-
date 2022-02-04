sub1 =int(input("Enter your first subject marks : "))
sub2 =int(input("Enter your second subject marks : "))
sub3 =int(input("Enter your third subject marks : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you failed bcoz you score is less than 33 ")
elif(sub1+sub2+sub3)/3 < 40 :
    print("your failed in this Exam ") 
else:
    print("Congrats ! you Crack the Exam")       
