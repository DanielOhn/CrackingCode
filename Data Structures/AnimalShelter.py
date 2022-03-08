from Queue import Queue
import random

class AnimalShelter():
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, item):
        print(item.animal, item.age)
        if (item.animal == "Dog"):
            self.dogs.add(item.age)
        elif(item.animal == "Cat"):
            self.cats.add(item.age)

    def dequeueAny(self, type=None):
        if (self.dogs.isEmpty() and self.cats.isEmpty()):
            return None
        elif (self.dogs.isEmpty()):
            return self.dequeueCat()
        elif (self.cats.isEmpty()):
            return self.dequeueDog()

        if (type is not None):
            if (type == "Dog"):
                return self.dequeueDog()
            else:
                return self.dequeueCat()

        if (self.dogs.peek() > self.cats.peek()):
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        return self.dogs.remove()

    def dequeueCat(self):
        return self.cats.remove()

    def getAnimals(self):
        return repr(self.dogs), repr(self.cats)

class Animal():
    def __init__(self, animal, age):
        self.animal = animal
        self.age = age 
    
    def getAge(self):
        return self.age

def createShelther():
    q = AnimalShelter()

    types = ["Dog", "Cat", None]

    for i in range(25):
        animal = Animal(animal=types[random.choice(range(0, 2))], age=i)
        q.enqueue(animal)
        #print(animal.animal, animal.age)

    print(q.getAnimals())

    rslt = ""
    for i in range(8):
       rslt += "{} > ".format(q.dequeueAny(type=types[random.choice(range(0, 3))]))
    
    print(rslt)
    print(q.getAnimals())
   
createShelther()
