from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)

indexPosition = 1
indexCheck = True

current = HeadNode
length = 0 

while current:
    length +=1
    if length == indexPosition:
        current.next = current.next.next
        break
    current = current.next
else:
    print("you give the index position is not found !!")
    indexCheck = False
    
if indexCheck:
    LinkedList.Display(HeadNode)
