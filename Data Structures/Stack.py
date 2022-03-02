class Stack():
    def __init__(self):
        self.top = None
        
    class StackNode():
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def pop(self):
        if (self.top.data == None):
            return "Empty stack"
            
        item = self.top.data
        self.top = self.top.next

        return item

    def push(self, item):
        node = self.StackNode(data=item, next=self.top)
        self.top = node
    
    def peek(self):
        return self.top.data
    
    def isEmpty(self):
        return self.top == None

    def __repr__(self):
        node = self.top
        rslt = ""

        while node is not None:
            rslt += "{} > ".format(node.data)
            node = node.next
        
        return rslt


class MinStack(Stack):
    def __init__(self):
        self.top = self.StackNode()
        self.small = self.StackNode()

    def pop(self):
        if (self.top == None):
            return "Empty list"

        val = self.top.data

        if (self.top == self.small):
            self.small = self.small.next
        
        self.top = self.top.next
        return val

    def push(self, item):
        node = self.StackNode(data=item)
        prev = self.top 

        self.top = node
        self.top.next = prev

        if (self.small.data == None or self.small.data >= item):
            prev = self.small
            self.small = node
            self.small.next = prev

    def min(self):
        return self.small.data

# stack = MinStack()

# print(stack.isEmpty())

# stack.push(1)
# print(stack.peek())
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.push(3.5)
# stack.push(0.5)
# print("Smallest: {}".format(stack.min()))

# print(stack.peek())
# print(repr(stack))
# print(stack.isEmpty())
# stack.pop()
# stack.peek()
# print("Smallest: {}".format(stack.min()))
