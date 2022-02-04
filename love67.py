# Make a snake water and gun game asking user to choose snake , water and Gun

import random

def gamewin(computer,you):
    if you == computer:
        return None
    elif computer ==  "s":
       if you == "w":
        return False
    elif you == "g":
        return True


    elif computer ==  "w":
       if you == "g":
        return True
    elif you == "s":
        return False

        
    elif computer ==  "g":
       if you == "s":
        return False
    elif you == "w":
        return True


Randno = random.randint(1, 3)
if Randno == 1:
    computer ="w"
elif Randno == 2:
    computer = "g"
elif Randno == 3:
    computer = "s"    

# print(Randno )


print("Computer turn : choose sanke(s) or water(w) or Gun(g) ?  ")
you = input("Your turn : choose snake(s) or water(w) or Gun(g) ? :  ")

a = gamewin(computer, you)  # computer and user data store in a--- Naming vari..


# print(f"computer choose {computer}")  # This is show what computer choose 
# print(f"You choose {you}")  # This statement show what user/you choose 

if a == None:
    print("The game is tie ")
elif a:
    print("You won with Computer")
else:
    print("You Loose !")
