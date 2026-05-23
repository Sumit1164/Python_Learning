from random import randint

class Railway:
    def __init__(self, pName, pAge, trainNo):
        self.pName = pName
        self.pAge = pAge
        self.trainNo = trainNo
        print(f"Hey, {pName}\nYour age is: {pAge}, Your train no is: {trainNo}")

    def book(self, froms, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {froms} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, froms, to):
        print(f"Ticket fare in train no: {self.trainNo} from {froms} to {to} is {randint(2465, 9854)}")

    
t = Railway("Sumit Tripathi", 22, 4363)
t.book("Gorakhpur", "Delhi")
t.getStatus()
t.getFare("Gorakhpur", "Delhi")