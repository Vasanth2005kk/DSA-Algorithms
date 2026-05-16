# (Remove Duplicates) ==> Delete repeated values from a sorted list

# Step 1: Import Linked List components
from LinkedListValue import HeadNode
from Display import LinkedList

# Step 2: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 3: Start from head
current = HeadNode

# Step 4: Traverse and compare adjacent nodes
while current and current.next:
    if current.data == current.next.data:
        # Step 5: Skip the duplicate node
        current.next = current.next.next
    else:
        # Step 6: Move to next node if no duplicate
        current = current.next

# Step 7: Display updated list
print("After Removing Duplicates:")
LinkedList.Display(HeadNode)

# Time Complexity: O(n)
# Reason: We traverse the list once.

# output --> After Removing Duplicates: [1|...] -> [2|...] -> [3|...] -> [4|...] -> 