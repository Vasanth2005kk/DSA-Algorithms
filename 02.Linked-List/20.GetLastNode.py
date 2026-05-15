from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)

current  = HeadNode

while current:
    lastNodeData = current.data
    current = current.next
    lastNodeNext = current

print()
print(f"Last Node ==> [{lastNodeData}|{str(lastNodeNext).split('x')[-1].strip('>')}]")