# using game() functiom make a game that store higher score in hiscore

def game():
    return 7

score = game()
with open("hiscore.txt", 'r') as file:
    hiScoreStr = file.read()

if hiScoreStr=='':
    with open("hiscore.txt", "w") as file:
        file.write(str(score))    


elif int(hiScoreStr)<score:
    with open("hiscore.txt", "w") as file:
        file.write(str(score))    
