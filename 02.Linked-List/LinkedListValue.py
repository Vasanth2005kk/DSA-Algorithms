# (Shared Values) ==> Common Linked List setup for all operations

# Step 1: Create a Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Step 2: Initialize nodes with sample values [1, 2, 3, 4, 2]
head = Node(1)
Node1 = Node(2)
Node2 = Node(3)
Node3 = Node(4)
Node4 = Node(2)

# Step 3: Link nodes together
head.next = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

# Step 4: Export HeadNode for other files to use
HeadNode = head

if __name__ == "__main__":
    from Display import LinkedList
    LinkedList.Display(head=HeadNode)

# Time Complexity: O(n) for setup