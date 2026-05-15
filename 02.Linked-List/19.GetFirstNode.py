from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)

FristNode = HeadNode

print()
print(f'Frist Node ==> [{FristNode.data}|{str(FristNode.next).split('x')[-1].strip('>')}]')