class Node():
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    def __repre__(self):
        return self.data

# Single Linked List
class LinkedList():
    def __init__(self):
        self.head = None

    def addNode(self, data):
        if (self.head == None):
            self.head = Node(data=data)
        else:
            node = self.head
            while node is not None:
                if (node.next == None):
                    node.next = Node(data=data)
                    break
                else:
                    node = node.next
    
    def removeNode(self, data):
        if (self.head == None):
            return "There are no nodes in this linked list"
        else:
            node = self.head
            while node is not None:
                temp = node.next
                if (temp.data == data):
                    temp.data = None
                    node.next = temp.next
                    break
                else:
                    node = node.next

    def __repr__(self):
        node = self.head
        rslt = ""

        while node is not None:
            rslt += "{} > ".format(node.data)
            node = node.next
        
        rslt += "None"
        
        return rslt

linked_list = LinkedList()
linked_list.addNode(5)
linked_list.addNode(2)
linked_list.addNode(4)

linked_list.removeNode(4)

print(repr(linked_list))