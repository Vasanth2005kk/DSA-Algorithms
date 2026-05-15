from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)
print()

OldValue = 320
UpdatedValue = 100

current = HeadNode

while current:
    if OldValue == current.data:
        current.data = UpdatedValue

    current =  current.next

LinkedList.Display(HeadNode)
