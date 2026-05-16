# (Update Operation) ==> Change the data of an existing node

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 3: Define values to update
OldValue = 320
UpdatedValue = 100
current = HeadNode

# Step 4: Traverse and update if value matches
while current:
    if OldValue == current.data:
        current.data = UpdatedValue
    current = current.next

# Step 5: Display updated list
print("Updated List:")
LinkedList.Display(HeadNode)

# Time Complexity: O(n)
# Reason: We must traverse the list to find the node(s) with the old value.

# output --> Updated List: [1|address] -> [2|address] -> ... 

