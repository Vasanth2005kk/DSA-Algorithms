# A general tree is a non-linear data structure where a parent node can have zero, two, or multiple child nodes without any limits. Key components include the root node, internal nodes, and leaf nodes

#        A
#      / | \
#     B  C  D
#    / \    |
#   E   F   G

# In this implementation, a TreeNode can have an unlimited number of children, stored in a Python list. The Tree class includes methods for adding, displaying, finding the length, and removing nodes.

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root =  None

    def add(self,data,parent=None) -> None:
        node = TreeNode(data)

        if not self.root:
            self.root =  node
            return
    
        if data and not parent:
            print("Parent Value You Are Not Assgined")
            return

        parentNode = self.findParent(
            ParentData=parent,
            node=self.root)

        if not parentNode:
            print("Parent Is Not Found !")
            return 
        
        parentNode.children.append(node)

    def findParent(self,ParentData,node):
        if node.data == ParentData:
            # print("parent node verfiy :",ParentData)
            return node

        for children in node.children:
            nodefound =  self.findParent(ParentData,children)
            if nodefound:
                return nodefound
        return None
    

    def display(self, node=None, prefix="", is_last=True):
        if node is None:
            node = self.root
            if not node:
                print("You Remove The Entire Tree")
                return
        
        if is_last:
            connector = "└── "  
        else :
            connector = "├── "

        print(prefix + connector + str(node.data))

        child_count = len(node.children)

        for i, child in enumerate(node.children):
            last = (i == child_count - 1)

            new_prefix = prefix + ("    " if is_last else "│   ")

            self.display(child, new_prefix, last)


    def length(self, node=None):
        if node is None:
            node = self.root

        count = 1  # current node

        for child in node.children:
            count += self.length(child)

        return count

    def remove(self,data,nodes=None):
        if self.root:
           nodes = self.root 

        if data == nodes.data:
            self.root = None
            return 

        findParent = self.findParentNode(data,self.root)

        if findParent:
            for i in findParent.children:
                if i.data == data:
                    findParent.children.remove(i)
                    return
        print("Not Found")


    def findParentNode(self,data,node):
        for child in node.children:
            if child.data == data:
                return node
            nodefound = self.findParentNode(data,child)
            if nodefound: 
                return nodefound
            
        return None

    
        


tree = Tree()
tree.add("A")

tree.add("B","A")
tree.add("C","A")
tree.add("D","A")

tree.add("K","B")
tree.add("V","B")

tree.add("E","D")
tree.add("F","D")

tree.add("R","V")

tree.display()
print("tree length :",tree.length())

tree.remove("A")
tree.display()
