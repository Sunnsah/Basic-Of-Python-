# ask students to enter marks and converter their marks into GPA

mark = float(input("Enter your marks : "))

if mark>=90:
    Grade = "A+"
elif mark>=80 :
    Grade = "A"
elif mark>=70 :
    Grade = "B+"
elif mark>=60 :
    Grade = "B"
else:
    Grade = "F"

print("your exam resulut is " + Grade)                
