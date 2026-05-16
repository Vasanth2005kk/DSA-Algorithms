# (Merge Operation) ==> Combine two sorted linked lists into one

# Step 1: Create two sorted lists
from LinkedListValue import Node
from Display import LinkedList

# First List: 10 -> 20 -> 30
head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)

# Second List: 15 -> 25 -> 35
head2 = Node(15)
head2.next = Node(25)
head2.next.next = Node(35)

print("List 1:")
LinkedList.Display(head1)
print("List 2:")
LinkedList.Display(head2)

# Step 2: Use a dummy node to simplify merging
dummy = Node(0)
tail = dummy

# Step 3: Compare heads of both lists and link the smaller one
while head1 and head2:
    if head1.data < head2.data:
        tail.next = head1
        head1 = head1.next
    else:
        tail.next = head2
        head2 = head2.next
    tail = tail.next

# Step 4: Append remaining nodes from either list
if head1:
    tail.next = head1
if head2:
    tail.next = head2

# Step 5: Display merged list
print("Merged Linked List:")
LinkedList.Display(dummy.next)

# Time Complexity: O(n + m)
# Reason: We traverse both lists once (n and m are lengths of the lists).

# output --> [10|...] -> [15|...] -> [20|...] -> [25|...] -> [30|...] -> [35|...] -> 