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

    # Add a node to the end of the linked list
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
    
    # Remove the first node in the linked list that matches the value
    def removeNode(self, data):
        if (self.head == None):
            return "There are no nodes in this linked list"
        else:
            node = self.head
            while node is not None:
                temp = node.next
                if (node.data == data):
                    self.head = node.next
                    node.data = None
                    break
                elif (temp.data == data):
                    temp.data = None
                    node.next = temp.next
                    break
                else:
                    node = node.next
    
    # Remove all duplicates within the linked list
    def removeDuplicates(self):
        if (self.head == None):
            return "No nodes in this linked list."
        else: 
            node = self.head
            values = []
            while node is not None:
                temp = node.next

                if (node.data not in values):
                    values.append(node.data)
                    node = node.next
                else:
                    self.removeNode(node.data)
                    node = node.next

    # Kth to last element
    def findKth(self, data):
        if (self.head == None):
            return "No Nodes in this biiitch"
        else:
            node = self.head
            result = ""
            found = False
            while node is not None:
                if (node.data == data and not found):
                    result += str(node.data)
                    found = True
                elif (found):
                    result += " > {0}".format(node.data)
                
                node = node.next
        
            return result

    # Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x
    def partitionNodes(self, val):
        if (self.head == None):
            return "Nope"
        else:
            node = self.head
            
            # Makes these linked list??
            less = LinkedList()
            great = LinkedList()

            while node is not None:
                if (node.data < val):
                    less.addNode(node.data)
                elif(node.data >= val):
                    great.addNode(node.data)
                
                node = node.next

            print("Partition Value: {0}".format(val))
            print(repr(less))
            print(repr(great))

            return less, great


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
linked_list.addNode(6)
linked_list.addNode(2)
linked_list.addNode(9)
linked_list.addNode(2)
linked_list.addNode(3)
linked_list.addNode(1)
print(repr(linked_list))

linked_list.removeDuplicates()

getNine = linked_list.findKth(9)
print(getNine)

linked_list.removeNode(5)

linked_list.partitionNodes(4)

print(repr(linked_list))