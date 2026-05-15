from LinkedListValue import HeadNode, Node
from Display import LinkedList

LinkedList.Display(HeadNode)

prev = None
current = HeadNode

while current:
    next_node =  current.next
    current.next = prev 
    prev = current
    current =  next_node

NewHead = prev

LinkedList.Display(NewHead)