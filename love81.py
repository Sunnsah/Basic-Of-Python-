class Employee:
    company = "Facebook"
    def getSalary(self):
        print("Salary is 80K ")
        print(f"David and Sunny Working in {self.company} as salary : {self.getSalary}")


David = Employee()
sunny = Employee()
David.getSalary()
sunny.getSalary()
sunny.salary = 8000
Employee.getSalary(David)
Employee.getSalary(sunny)


