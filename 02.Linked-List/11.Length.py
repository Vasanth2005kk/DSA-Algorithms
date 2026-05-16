# (Length Operation) ==> Count the number of nodes in the list

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display the list
print("Linked List:")
LinkedList.Display(HeadNode)

# Step 3: Initialize counter and start from head
Length = 0
current = HeadNode

# Step 4: Traverse and increment counter for each node
while current:
    Length += 1
    current = current.next

# Step 5: Print total length
print(f"Total Linked List Length: {Length}")

# Time Complexity: O(n)
# Reason: We must visit every node to count it.

# output --> Total Linked List Length: 5