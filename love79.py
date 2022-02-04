class RailwayForm:
    type = "Form"
    def printdata(self):
        print(f"Name is : {self.name}")
        print(f"Train name is {self.Train}")

Davidapplication = RailwayForm()
Davidapplication.name = "SunnY Kumar Sah"
Davidapplication.Train = "JanakPurTrain"
Davidapplication.printdata()
