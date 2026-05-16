# (Insert End) ==> Add a new node at the very end

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Value to insert
Value = 100
lastNode = Node(Value)

# Step 3: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 4: Traverse to the last node
current = HeadNode
while current is not None:
    if current.next is None:
        # Step 5: Link last node's next to new node
        current.next = lastNode
        break
    current = current.next

# Step 6: Display updated list
print("Updated List:")
LinkedList.Display(HeadNode)

# Time Complexity: O(n)
# Reason: We must traverse the entire list to find the last node.

# output --> [1|address] -> [2|address] -> [3|address] -> [4|address] -> [100|None] -> 

