class LinkedList:
    def __init__(self):
        pass

    def Display(self,head):

        current =  head 
        
        while current:
            print(f'[{current.data}|{current.next}]')
            current =  current.next
