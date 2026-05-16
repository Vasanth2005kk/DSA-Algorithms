# (Insert Beginning) ==> Add a new node at the start

# Step 1: Import HeadNode and Node
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: New value to insert
Value = 100

# Step 3: Create new node and point its next to current head
FirstNode = Node(Value)
FirstNode.next = HeadNode 

# Step 4: Display the updated list
LinkedList.Display(FirstNode)

# Time Complexity: O(1)
# Reason: Only one pointer update is needed, regardless of list size.

# output --> [100|address] -> [1|address] -> [2|address] -> [3|address] -> [4|address] -> 