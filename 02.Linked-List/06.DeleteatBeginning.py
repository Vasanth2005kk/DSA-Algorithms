# (Delete Beginning) ==> Remove the first node

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 3: Shift head to the next node
current = HeadNode
HeadNode = current.next

# Step 4: Display updated list
print("Updated List:")
LinkedList.Display(HeadNode)

# Time Complexity: O(1)
# Reason: Only the head pointer needs to be updated.

# output --> [2|address] -> [3|address] -> [4|address] -> 