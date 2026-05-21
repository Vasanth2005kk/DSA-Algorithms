# (Priority Queue Implementation) ==> Higher priority removed first

class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item, priority):
        # We store items as a tuple: (priority, item)
        self.queue.append((priority, item))
        # Sort based on priority
        # Let's assume a smaller number means higher priority (e.g., Priority 1 is before Priority 2)
        self.queue.sort(key=lambda x: x[0])
        print(f"Enqueued: {item} with priority {priority}")
        
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed[1]} (Priority {removed[0]})")
            return removed[1]
        else:
            print("Queue is Empty")
            
    def is_empty(self):
        return len(self.queue) == 0
        
    def display(self):
        print("Priority Queue [(Priority, Item)]:", self.queue)

# Example Usage
if __name__ == "__main__":
    print("--- Priority Queue ---")
    pq = PriorityQueue()
    pq.enqueue("Normal Task A", 3)
    pq.enqueue("Urgent Task B", 1)  # Higher priority, should be removed first
    pq.enqueue("Important Task C", 2)
    pq.display()
    
    pq.dequeue()  # Removes Urgent Task B
    pq.display()
