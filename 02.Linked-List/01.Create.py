# Create a node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


head = Node(10)

Node1 =  Node(20)
head.next  = Node1

Node2 = Node(30)
Node1.next =  Node2

Node3 = Node(40)
Node2.next = Node3

if __name__ == "__main__":
    from Display import LinkedList
    LinkedList.Display(head)