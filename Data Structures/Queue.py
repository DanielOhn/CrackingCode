class Queue():
    def __init__(self):
        self.first = None
        self.last = None 
    
    class QueueNode():
        def __init__(self, data=None, next=None):
            self.data = data 
            self.next = next
    
    def add(self, item):
        node = self.QueueNode(data=item)
        if (self.last != None):
            self.last.next = node
        
        self.last = node

        if (self.first == None):
            self.first = node 


    def remove(self):
        if (self.first == None):
            return "No nodes in this Q"
        
        data = self.first.data 
        self.first = self.first.next

        if (self.first == None):
            self.last = None
        
        return data

    def peek(self):
        if (self.first == None):
            return "No nodes in this Q"
        return self.first.data

    def isEmpty(self):
        return self.first == None

q = Queue()
print(q.isEmpty())
q.add(1)

print(q.peek())

q.add(2)
q.add(3)
q.remove()
print(q.peek())
q.remove()
print(q.peek())