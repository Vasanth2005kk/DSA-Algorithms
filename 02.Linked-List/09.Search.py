# (Search Operation) ==> Find a value in the linked list

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display the list
print("Linked List:")
LinkedList.Display(HeadNode)

# Step 3: Value to search for
SearchValue = 7
current = HeadNode

# Step 4: Traverse and compare each node's data
while current:
    if SearchValue == current.data:
        print(f"Result: Value {SearchValue} was FOUND!")
        break
    current = current.next
else:
    # Step 5: Handle value not found
    print(f"Result: Value {SearchValue} was NOT FOUND.")

# Time Complexity: O(n)
# Reason: We may need to check every node in the list.

# output --> Result: Value 7 was NOT FOUND.

