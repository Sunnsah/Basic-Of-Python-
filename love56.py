# Function and Recursion of chapter *


#list of marks ---1----
Marks = [77,55,80,78]
percentage = (sum(Marks)/400)*100
print(percentage)

#list of marks ---2--- Students
Marks1 = [70,59,87,70]
percentage1 = (sum(Marks1)/400)*100
print(percentage1)

#use of + operator not sum

marks = [90,66,66,88,90]
percantage10 = ((marks[0] + marks[1] + marks[2]+ marks[3] + marks[4])/500)*100
print(percantage10)


# define 

def percent(marks):
   p = ((marks[0] + marks[1] + marks[2]+ marks[3] + marks[4])/500)*100
   return p

marks10 = [77,70,80,90,75]
percentage2 = percent(marks10)
print(percentage2)





