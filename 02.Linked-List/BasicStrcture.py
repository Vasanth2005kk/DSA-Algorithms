# STEP 1 : Create Node class

class Node:
    # constructor function
    def __init__(self, data):

        # store value inside node
        self.data = data

        # next node address
        self.next = None

# STEP 2 : Create Nodes

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)


# Memory Structure After Creation

# node1 = [10 | None]
# node2 = [20 | None]
# node3 = [30 | None]

# STEP 3 : Connect Nodes

node1.next = node2
node2.next = node3

# Structure becomes:

# node1 -> node2 -> node3 -> None
#
# Visual Memory View
#
# node1
# ┌──────┬────────┐
# │ 10   │   •────┼──► node2
# └──────┴────────┘
# node2
# ┌──────┬────────┐
# │ 20   │   •────┼──► node3
# └──────┴────────┘
# node3
# ┌──────┬────────┐
# │ 30   │  None  │
# └──────┴────────┘

# STEP 4 : Start Traversing

# current variable points to first node
current = node1

# STEP 5 : Traverse using while loop

while current:

    # print current node data
    print("Current Data :", current.data)

    # print next node reference
    print("Next Address :", current.next)
    print("---------------------")

    # move to next node
    current = current.next


# FINAL OUTPUT
#
# Current Data : 10
# Next Address : <__main__.Node object at 0x...>
#
# Current Data : 20
# Next Address : <__main__.Node object at 0x...>
#
# Current Data : 30
# Next Address : None
#
#
# Traversal Flow
#
# current = node1
#          ↓
#        node2
#          ↓
#        node3
#          ↓
#         None
#
#
# Simple Flow
#
# 10 -> 20 -> 30 -> None