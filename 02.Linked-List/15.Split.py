# (Split Operation) ==> Divide the linked list into two halves

# Step 1: Import components and use slow/fast pointers
from LinkedListValue import HeadNode
from Display import LinkedList

slow = HeadNode
fast = HeadNode.next

# Step 2: Traverse to find the middle point
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# Step 3: Split the list into two parts
second_half = slow.next
slow.next = None

# Step 4: Display both halves
print("First Half:")
LinkedList.Display(HeadNode)

print("Second Half:")
LinkedList.Display(second_half)

# Time Complexity: O(n)
# Reason: We traverse the list once to find the middle.

# output --> First Half: [1|...] -> [2|...] -> \n Second Half: [3|...] -> [4|...] -> 