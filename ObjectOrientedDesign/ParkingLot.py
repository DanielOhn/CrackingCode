class Parking():
    def __init__(self, lot, occupied, assigned):
        self.lot = lot
        self.occupied = occupied
        self.assigned = assigned

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model

class ParkingLot():

    def __init__(self):
        self.queue = []
        self.lots = self.setLots()
        self.assigned = []

    def addQueue(self, car):
        if (car):
            self.queue.append(car)
            return self.queue 

    def setLots(self):
        letters = ['A', 'B', 'C', 'D', 'E']
        lots = []

        for i in range(len(letters)):
            for j in range(12):
                lot = "{0}{1}".format(letters[i], str(j))
                park = Parking(lot, False, None)
                lots.append(park)

        return lots

    def assignParking(self, car):
        if (len(self.queue) > 0):
            for lot in len(self.lots):
                if (lot.occupied == False):
                    lot.occupied = True
                    lot.assigned = car
                    print(lot.lot, lot.occupied, lot.assigned)
                    return lot
                else:
                    print("Parking Lot is full")
    
    def __str__(self):
        s = ""

        for lot in self.lots:
            s += "{0} - Occupied: {1} by {2}\n".format(lot.lot, lot.occupied, lot.assigned)

        return s


park = ParkingLot()
print(park)
