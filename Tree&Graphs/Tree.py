class Node():
    def __init__(self, name=None, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


class Tree():
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
            
    
    def inOrderTraversal(self, node):
        if (node != None):
            self.inOrderTraversal(node.left)
            self.visit(node)
            self.inOrderTraversal(node.right)

    def visit(self, node):
        print("{}".format(node.name))
        return node.name

    def printTree(self):
        return self.inOrderTraversal(self.root)
    
def createTree():
    nums = [3, 5, 7, 9, 8]

    tree = Tree(Node(name=6))

    for i in nums:
        num = Node(name=i)
        tree.add(num)
    
    tree.printTree()

createTree()

    

