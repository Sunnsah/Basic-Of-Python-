#Constructor in Oops

class Employee:
    company = "Daraz"

    def __init__( self,name,salary,subUnit ):
        self.name = name
        self.salary = salary
        self.subUnit = subUnit

        print("Employee is Created Using Init ")

    def GetsDetails(self):
        print(f"name is {self.name}")
        print(f"Salary is {self.salary}")
        print(f"Subunites is {self.subUnit}")



david = Employee("sunny", 899, "Printers")  
david.GetsDetails()     