# (Detect Loop) ==> Check if the linked list has a cycle

# Step 1: Import HeadNode
from LinkedListValue import HeadNode

# Step 2: Use slow and fast pointers (Floyd's Cycle-Finding Algorithm)
slow = HeadNode
fast = HeadNode
isLoop = False

# Step 3: Traverse the list
while fast and fast.next:
    slow = slow.next          # Move 1 step
    fast = fast.next.next     # Move 2 steps

    # Step 4: If pointers meet, a loop exists
    if slow == fast:
        isLoop = True
        break

# Step 5: Print result
print(f"Loop Found: {isLoop}")

# Time Complexity: O(n)
# Reason: In the worst case, we traverse the list proportional to its size.

# output --> Loop Found: False