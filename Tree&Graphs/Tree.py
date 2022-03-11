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
    print()

    print("REturned: {}".format(tree.remove(9)))
    tree.printTree()

createTree()

    

