class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"Seats are available in train are {self.seats} ")

    def fareInfo(self):
        print(f"The price of the ticket is Rs.{self.fare}")

    def bookTicket(self):
        if self.seats>0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry the train is full! Kindely try for tatkal.")

        
intercity = Train("Intercity Express : 23450", 150, 3)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
