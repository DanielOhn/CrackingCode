from audioop import reverse
from Stack import Stack

class QueueWithStacks():
    def __init__(self):
        self.mainStack = Stack()
        self.reverseStack = Stack()

    def push(self, item):
        self.mainStack.push(item)

        if (self.reverseStack.top == None):
            self.reverseStack.push(item)
        else:
            node = Stack.StackNode(data=item)
            tempNode = self.reverseStack.top

            while tempNode is not None:
                if (tempNode.next == None):
                    tempNode.next = node
                    break

                tempNode = tempNode.next
    
    def pop(self):
        node = self.reverseStack.top
        itr = self.mainStack.top 

        self.reverseStack.top = self.reverseStack.top.next

        while itr is not None:
            nxt = itr.next

            if (nxt.data == node.data):
                itr.next = None
                break
            
            itr = itr.next

        return node.data

    def peek(self):
        return self.reverseStack.top.data


    def printQ(self):
        return repr(self.reverseStack)
    
    def isEmpty(self):
        return self.reverseStack.top == None


def createQueue():
    q = QueueWithStacks()

    print(q.isEmpty())

    for i in range(10):
        q.push(i)
    
    print(q.printQ())

    print(q.pop())
    print(q.printQ())
    print(q.peek())
    print(q.isEmpty())



createQueue()