from LinkedListValue import HeadNode,Node
from Display import LinkedList

Value = 100
Index = 2

new_Node = Node(Value)


# print the linkedList
LinkedList.Display(HeadNode)


Current =  HeadNode # HeadNode default store 4 node values like (1,2,3,4)
length = 0

while(Current is not None):
    length += 1
    if length == Index:
        new_Node.next = Current.next
        Current.next = new_Node
        break

    Current = Current.next

LinkedList.Display(HeadNode)
