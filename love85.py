# Oops Question number : 5

from traceback import FrameSummary


class Train:
    def __init__(self, name, seats,fare):

        self.name = name
        self.fare = fare
        self.seats = seats
        
    def GetStatus(self):
        print(f"The Train {self.name} you booked ")
        print(f"The Seats is Avalibale in {self.name } is {self.seats}")

    def FareInfo(self):
        print(f"The price of Train is Rs: {self.fare}")   

        
    def GetBook(self):
        if(self.seats>0):
            print(f"You booked Train Name is {self.name} and Seats numer is {self.seats} at cost Rs:  {self.fare}")
            self.seats = self.seats-1
        else:
            print(f"Sorry ! The Train name of {self.name} is Full : Kindly Try in Takkal ")


    def CancelTickets(self):
        pass

Janakpurcity = Train("JanakpurCity", 100, 90)
Janakpurcity.GetStatus()
Janakpurcity.GetBook()       
Janakpurcity.GetBook()        
Janakpurcity.GetBook()        

