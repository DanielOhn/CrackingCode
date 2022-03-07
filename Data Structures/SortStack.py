from Stack import Stack

class SortStack():
    def __init__(self):
        self.stack = Stack()
        self.sorted = Stack()
    
    def sort(self):
        tempStack = self.sorted

        while (not self.stack.isEmpty()):
            node = self.stack.pop() 

            while (not tempStack.isEmpty() and tempStack.top.data < node):
                temp = tempStack.pop() 
                self.stack.push(temp)

            tempStack.push(node)
        
        self.stack = tempStack
        return tempStack

    def push(self, item):
        self.stack.push(item)

    def getStack(self):
        return repr(self.stack)
        

def createStack():
    stack = SortStack()

    for i in range(10):
        stack.push(i)

    print(stack.getStack())
    print(stack.sort())

createStack()