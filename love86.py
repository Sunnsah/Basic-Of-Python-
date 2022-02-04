# Use @Propertry class -- Function ---

from email.message import EmailMessage


class Employee:
    company = "Nepal Gas"
    Salary = 7000
    BonusSalary = 700


    @property
    def TotalSalary(self):
        return self.Salary + self.BonusSalary

    @TotalSalary.setter
    def TotalSalary(self, val):    
        self.BonusSalary = val - self.Salary

mohan = Employee()
print(mohan.TotalSalary)    
mohan.TotalSalary = 8000
# print(mohan.TotalSalary)
print(mohan.BonusSalary)
print(mohan.Salary)
