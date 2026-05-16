# (Insert at Position) ==> Add a new node at a specific index

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Value and Position
Value = 100
Index = 2
new_Node = Node(Value)

# Step 3: Display original list
print("Original List:")
LinkedList.Display(HeadNode)

# Step 4: Traverse to the target position
Current = HeadNode
length = 0

while Current is not None:
    length += 1
    if length == Index:
        # Step 5: Insert the node by updating pointers
        new_Node.next = Current.next
        Current.next = new_Node
        break
    Current = Current.next

# Step 6: Display updated list
print("Updated List:")
LinkedList.Display(HeadNode)

# Time Complexity: O(n)
# Reason: In the worst case, we might need to traverse to the end of the list.

# output --> [1|address] -> [2|address] -> [100|address] -> [3|address] -> [4|address] -> 

