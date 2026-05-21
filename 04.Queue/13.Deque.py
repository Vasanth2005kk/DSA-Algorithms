# (Double Ended Queue / Deque Implementation) ==> Insert/Delete both ends

class Deque:
    def __init__(self):
        self.deque = []
        
    def insert_front(self, item):
        self.deque.insert(0, item)
        print(f"Inserted at front: {item}")
        
    def insert_rear(self, item):
        self.deque.append(item)
        print(f"Inserted at rear: {item}")
        
    def delete_front(self):
        if not self.is_empty():
            removed = self.deque.pop(0)
            print(f"Deleted from front: {removed}")
            return removed
        else:
            print("Deque is Empty")
        
    def delete_rear(self):
        if not self.is_empty():
            removed = self.deque.pop()
            print(f"Deleted from rear: {removed}")
            return removed
        else:
            print("Deque is Empty")
            
    def is_empty(self):
        return len(self.deque) == 0
        
    def display(self):
        print("Deque:", self.deque)

# Example Usage
if __name__ == "__main__":
    print("--- Double Ended Queue (Deque) ---")
    dq = Deque()
    
    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)  # Add to front
    dq.display()
    
    dq.delete_rear()    # Remove from rear
    dq.display()
