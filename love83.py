# Oops Question no.1

class Programmer:
    company = "Daraz"
    
    def __init__(self, name , product):
        self.name = name
        self.product = product

    def getinfo(self):
            print(f"The Programmer of {self.company} is {self.name} Working on {self.product}")

David = Programmer("David", "Google Cloud")
Lucky = Programmer("Lucky", "ZooM")
David.getinfo()
Lucky.getinfo()

