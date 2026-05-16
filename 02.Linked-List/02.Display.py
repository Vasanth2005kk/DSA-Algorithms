# (Display Operation) ==> Visit and print all elements

class LinkedList:
    def __init__(self):
        pass

    # Step 1: Define display method
    def Display(self, head):
        # Step 2: Start from head
        current = head 
        
        # Step 3: Traverse until end (None)
        while current:
            print(f'[{current.data}|{current.next}]')
            current = current.next

# Time Complexity: O(n)
# Reason: We must visit every node once to display it.

