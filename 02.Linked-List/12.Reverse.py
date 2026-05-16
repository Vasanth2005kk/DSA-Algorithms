# (Reverse Operation) ==> Flip the linked list direction

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 3: Initialize pointers (prev, current, next)
prev = None
current = HeadNode

# Step 4: Traverse and reverse pointers
while current:
    next_node = current.next  # Store next node
    current.next = prev       # Reverse link
    prev = current            # Move prev forward
    current = next_node       # Move current forward

# Step 5: Update head to the new front (prev)
NewHead = prev

# Step 6: Display reversed list
print("Reversed List:")
LinkedList.Display(NewHead)

# Time Complexity: O(n)
# Reason: We visit each node exactly once to update its pointer.

# output --> Reversed List: [4|address] -> [3|address] -> [2|address] -> [1|address] -> 