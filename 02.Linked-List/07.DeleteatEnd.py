# (Delete End) ==> Remove the last node

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 3: Traverse to the second-to-last node
current = HeadNode
while current is not None:
    # Step 4: Check if next node is the last node
    if current.next.next == None:
        # Step 5: Set current's next to None to delete the last node
        current.next = None
        break
    current = current.next

# Step 6: Display updated list
print("Updated List:")
LinkedList.Display(HeadNode)

# Time Complexity: O(n)
# Reason: We must traverse to the second-to-last node to update its pointer.

# output --> [1|address] -> [2|address] -> [3|address] -> 