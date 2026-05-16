# (Create Operation) ==> Create a basic linked list

# Step 1: Create a Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Step 2: Initialize nodes
head = Node(10)
Node1 = Node(20)
Node2 = Node(30)
Node3 = Node(40)

# Step 3: Link nodes to form a list
head.next = Node1
Node1.next = Node2
Node2.next = Node3

# Step 4: Display the Linked List
if __name__ == "__main__":
    from Display import LinkedList
    LinkedList.Display(head)

# Time Complexity: O(n)
# Reason: Creating n nodes and linking them takes linear time.

# output --> [10|address] -> [20|address] -> [30|address] -> [40|address] -> 