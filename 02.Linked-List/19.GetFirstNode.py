# (Get First Node) ==> Access the very first element of the list

# Step 1: Import Linked List components
from LinkedListValue import HeadNode, Node
from Display import LinkedList

# Step 2: Display the list
print("Linked List:")
LinkedList.Display(HeadNode)

# Step 3: Access the head node
FirstNode = HeadNode

# Step 4: Print node details
print(f"First Node Data: {FirstNode.data}")
print(f"Next Node Address: {str(FirstNode.next).split('x')[-1].strip('>')}")

# Time Complexity: O(1)
# Reason: Accessing the head is a direct operation.

# output --> First Node Data: 1