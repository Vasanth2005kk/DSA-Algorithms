from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)

current = HeadNode
HeadNode = current.next

LinkedList.Display(HeadNode)