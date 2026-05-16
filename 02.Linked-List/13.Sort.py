# (Sort Operation) ==> Arrange nodes in ascending order

# Step 1: Create an unsorted linked list
from LinkedListValue import Node
from Display import LinkedList

head = Node(3)
node1 = Node(2)
head.next = node1
node2 = Node(1)
node1.next = node2
node3 = Node(4)
node2.next = node3

# Step 2: Display original list
print("Original List:")
LinkedList.Display(head)

# Step 3: Bubble Sort (Nested Loops)
current = head
while current:
    index = current.next
    while index:
        # Step 4: Swap data if current > next
        if current.data > index.data:
            current.data, index.data = index.data, current.data
        index = index.next
    current = current.next

# Step 5: Display sorted list
print("Sorted List:")
LinkedList.Display(head)

# Time Complexity: O(n^2)
# Reason: Nested loops are used to compare every pair of nodes.

# output --> Sorted List: [1|address] -> [2|address] -> [3|address] -> [4|address] -> 

