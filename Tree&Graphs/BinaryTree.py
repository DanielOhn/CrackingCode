class Node():
    def __init__(self, name=None, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self, root):
        self.root = root

    def add(self, node):

        if (self.root == None):
            self.root = node

        c = self.root

        while c is not None:        
            if (c.name > node.name and c.left == None):
                c.left = node
                break
            elif(c.name > node.name):
                c = c.left

            if (c.name < node.name and c.right == None):
                c.right = node
                break
            elif (c.name < node.name):
                c = c.right

    # Removes the node and all it's children
    # NEed to remove just the node and swap out for the children value
    def remove(self, value):
        if (self.root == None):
            return None

        node = self.root

        while node is not None:
            if (node.left != None):
                if (node.left.name == value):
                    node.left = None 
                    return node.name
            elif (node.right != None):
                if (node.right.name == value):
                    node.right = None 
                    return node.name
            
            if (node.name < value):
                node = node.right
            if (node.name > value):
                node = node.left

    def getMinKey(self, node):
        while node.left:
            node = node.left
        return node
    
    def deleteNode(self, key):
        parent = None
        curr = self.root

        while curr and curr.name != key:
            parent = curr

            if key < curr.name:
                curr = curr.left
            else:
                curr = curr.right
            
        if curr is None:
            return self.root
        
        if curr.left is None and curr.right is None:
            if curr != self.root:
                if parent.left == curr:
                    parent.left = None
                else:
                    parent.right = None
            else:
                root = None
        elif curr.left and curr.right:
            successor = self.getMinKey(curr.right)
            val = successor.name
            self.deleteNode(root, successor.name)
            curr.name = val
        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right
            if curr != self.root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
        return self.root

    
    def inOrderTraversal(self, node):
        if (node != None):
            self.inOrderTraversal(node.left)
            self.visit(node)
            self.inOrderTraversal(node.right)
    
    def preOrderTraversal(self, node):
        if (node != None):
            self.visit(node)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if (node != None):
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            self.visit(node)

    def visit(self, node):
        print("{}".format(node.name))
        return node.name

    def printTree(self):
        return self.inOrderTraversal(self.root)
    
def createTree():
    nums = [3, 5, 7, 9, 8]

    tree = BinaryTree(Node(name=6))

    for i in nums:
        num = Node(name=i)
        tree.add(num)
    
    tree.printTree()
    print("\n")

    tree.deleteNode(9)
    tree.printTree()

createTree()

    

