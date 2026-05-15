from LinkedListValue import HeadNode,Node
from Display import LinkedList

LinkedList.Display(HeadNode)
print()


SearchValue =  7

current = HeadNode


while current:
    if SearchValue == current.data:
        print(f"Your Search Value {SearchValue} Is Founded")
        break
    current =  current.next
else:
    print(f"Your Search Value {SearchValue} Is Not Founded")
