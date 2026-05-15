class LinkedList():
    def Display(head):

        current = head 
        
        while current:
            print(f'[{current.data}|{str(current.next).split('x')[-1].strip('>')}]',end=' -> ')
            current =  current.next

        print()