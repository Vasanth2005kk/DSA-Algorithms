from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)

current = HeadNode

while(current is not None):
    if current.next.next == None:
        current.next = None
        break
    current = current.next


LinkedList.Display(HeadNode)