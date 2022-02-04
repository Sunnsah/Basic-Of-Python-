

print(" ****Welcome to Computer Quiz Game**** ")
playing = input("Do you play Computer Game : ").lower()
if playing  != "yes":
    quit()
    # print("Okay, Let's Play ----Quiz Game----")
    

answer = input("What does CPU stands for :  ").lower()
if answer == "central processing unit":
    print("Correct ! you got one point .")
else:
    print("InCorrect !!! ")

answer = input("What does IC stands for :  ").lower()
if answer == "integrated circuit":
    print("Correct ! you got second  point .")
else:
    print("InCorrect !!! ")    

answer = input("What does AC stands for :  ").lower()
if answer == "accumulator register":
    print("Correct ! you got Third point .")
else:
    print("InCorrect !!! ")   

answer = input("What does CU stands for :  ").lower()
if answer == "control unit":
    print("Correct ! you got Fourth point .")
else:
    print("InCorrect !!! ")     

answer = input("What does IDE stands for :  ").lower()
if answer == "integrated development enviroment":
    print("Correct ! you got one point .")
else:
    print("InCorrect !!! ")    



