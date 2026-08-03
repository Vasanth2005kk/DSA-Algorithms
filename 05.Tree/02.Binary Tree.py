class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,data):
        if not self.root:
            self.root = Node(data)
            return

        self.recursiveAdd(data,self.root)

    def recursiveAdd(self,data, node):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self.recursiveAdd(data,node.left)

    def display(self,depth=0,node=None):
        if not node:
            node = self.root

        print(" "*depth,node.data)

        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)

    def remove(self,data):
        if not self.root:
            print("Binary Tree is Empty")
            return

        if self.root.data == data:
            self.root = None
            return

        self.recursiveRemove(data,self.root)

    def recursiveRemove(self,data,node):
        if node.left and node.left.data == data:
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None
            return

        if node.left:
            self.recursiveRemove(data,node.left)
        if node.right:
            self.recursiveRemove(data,node.right)

    def search(self,data):
        nodefound = self.recursiveSearch(data,self.root)
        if nodefound: print("True")
        else: print("False")

    def recursiveSearch(self,data,node):
        if not node or node.data == data:
            return node

        return self.recursiveSearch(data,node.left) or self.recursiveSearch(data,node.right)




binaryTree = BinaryTree()
binaryTree.add(5)
binaryTree.add(1)
binaryTree.add(2)
binaryTree.add(3)
binaryTree.add(4)
binaryTree.add(5)
binaryTree.display()
binaryTree.remove(4)
binaryTree.display()
binaryTree.search(3)

