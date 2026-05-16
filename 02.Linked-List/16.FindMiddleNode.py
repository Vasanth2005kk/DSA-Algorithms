# (Find Middle Node) ==> Locate the central node using two pointers

# Step 1: Import Linked List components
from LinkedListValue import HeadNode
from Display import LinkedList

# Step 2: Display the list
print("Linked List:")
LinkedList.Display(HeadNode)

# Step 3: Use slow and fast pointers (Hare and Tortoise algorithm)
slow = HeadNode
fast = HeadNode

# Step 4: Traverse the list
while fast and fast.next:
    slow = slow.next          # Move 1 step
    fast = fast.next.next     # Move 2 steps

# Step 5: When fast reaches end, slow is at the middle
print(f"Middle Node Data: {slow.data}")

# Time Complexity: O(n)
# Reason: We traverse the list once.

# output --> Middle Node Data: 3