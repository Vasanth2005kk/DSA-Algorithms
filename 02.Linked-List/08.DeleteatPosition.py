# (Delete at Position) ==> Remove node at a specific index

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 3: Position to delete
indexPosition = 1
indexCheck = True
current = HeadNode
length = 0 

# Step 4: Traverse to the position before target
while current:
    length += 1
    if length == indexPosition:
        # Step 5: Skip the target node
        current.next = current.next.next
        break
    current = current.next
else:
    # Step 6: Handle index out of bounds
    print("Error: Index position not found!")
    indexCheck = False
    
# Step 7: Display updated list if successful
if indexCheck:
    print("Updated List:")
    LinkedList.Display(HeadNode)

# Time Complexity: O(n)
# Reason: In the worst case, we might traverse the entire list.

# output --> [1|address] -> [3|address] -> [4|address] -> 

