#Question no.2

class Calculator:
    def __init__(self,num) :
        self.num = num

    def square(self):
        print(f"The number is {self.num} of Square is {self.num **2}")  

    def squareroot(self):
        print(f"The number is {self.num} of Squareroot is {self.num **0.5}")    
        
    def cube(self):
        print(f"The number is {self.num} of Cube is {self.num **3}")    
        

d7 = Calculator(7)
d7.square()
d7.cube()
d7.squareroot()