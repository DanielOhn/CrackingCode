from Stack import Stack

class MaxStack(Stack):
    def __init__(self, max=5):
        self.plates = []
        self.max = max
        self.count = 0
    
    def push(self, item):
        if (self.count % self.max == 0):
            self.plates.append(Stack())
        
        current = self.plates[len(self.plates) - 1]

        current.push(item)
        self.count = self.count + 1

    def pop(self):
        data = self.plates[len(self.plates) - 1].top.data
        self.plates[len(self.plates) - 1].pop()

        if (self.count % self.max == 1):
            self.plates.remove(self.plates[len(self.plates) - 1])
        
        self.count = self.count - 1
        return data
    
    def getStacks(self):
        for i in range(len(self.plates)):
            print(repr(self.plates[i]))
        print('\n')
    
def getStack():
    stack = MaxStack(5)

    for i in range(15):
        stack.push(i)
    
    stack.getStacks()

    for i in range(6):
        print(stack.pop())
    print("\n")
    stack.getStacks()

getStack()