class Employee:
    company = "Google"
    Salary = 900 # Class attibutes


sunny = Employee() 
Ganesh = Employee()
sunny.Salary = 850
print(sunny.Salary) #Instance Attibutes
print(sunny.company)
print(Ganesh.company)   
Employee.company = "MicroSoft"
print(Ganesh.company)   
print(sunny.company)
