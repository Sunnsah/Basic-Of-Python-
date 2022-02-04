# Ask student to enter their marks and show them [pass and fail at least 33% ]

sub1 = int(input("Enter a Math mark: "))
sub2 = int(input("Enter a Computer mark: "))
sub3 = int(input("Enter a Account mark: "))

if(sub1>=40):
    print("Pass in Math  " + str(sub1))
else:
    print("Fail in Math  " +  + str(sub1))
if(sub2>=40):     
    print("pass in Computer "  + str(sub2))
else:
    print("Fail in Computer "  + str(sub2))
if(sub3>=40):
    print("pass in Account "  + str(sub3))
else:
    print("Fail in Account "  + str(sub3))      

print("Congrats ! You need to improve")       
