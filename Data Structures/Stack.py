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


stack = Stack()

print(stack.isEmpty())

stack.push(1)
print(stack.peek())
stack.push(2)
stack.push(3)
print(stack.peek())

print(stack.isEmpty())
print(stack.pop())
print(stack.peek())

