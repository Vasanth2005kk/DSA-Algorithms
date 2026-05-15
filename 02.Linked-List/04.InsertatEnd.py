from LinkedListValue import HeadNode,Node
from Display import LinkedList

Value = 100

lastNode = Node(Value)
LinkedList.Display(HeadNode)

current =  HeadNode
while current is not None:
    if current.next is None:
        current.next = lastNode
        break

    current = current.next

LinkedList.Display(HeadNode)
