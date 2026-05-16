# (Get Last Node) ==> Access the very last element of the list

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display the list
print("Linked List:")
LinkedList.Display(HeadNode)

# Step 3: Traverse to the end
current = HeadNode
lastNodeData = None
lastNodeNext = None

while current:
    lastNodeData = current.data
    lastNodeNext = current.next
    current = current.next

# Step 4: Print node details
print(f"Last Node Data: {lastNodeData}")
print(f"Next Node Address: {str(lastNodeNext).split('x')[-1].strip('>')}")

# Time Complexity: O(n)
# Reason: We must traverse the entire list to find the last node.

# output --> Last Node Data: 4