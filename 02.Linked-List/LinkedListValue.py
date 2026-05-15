# Linked List Values 
# [1,2,3,4]


# Create a node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


head = Node(1)

Node1 =  Node(2)
head.next  = Node1

Node2 = Node(3)
Node1.next =  Node2

Node3 = Node(4)
Node2.next = Node3


HeadNode =  head


if __name__ == "__main__":
    from Display import LinkedList
    LinkedList.Display(head=HeadNode)