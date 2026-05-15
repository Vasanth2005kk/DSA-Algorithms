from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)
print()

Length = 0
current = HeadNode

while current:
    Length+=1
    current =  current.next

print(f"LinkedList Length :{Length}")