# (Simple Queue Implementation) ==> Normal FIFO queue

class SimpleQueue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
        
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is Empty")
            
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Empty"
        
    def is_empty(self):
        return len(self.queue) == 0
        
    def display(self):
        print("Queue:", self.queue)

# Example Usage
if __name__ == "__main__":
    print("--- Simple Queue ---")
    sq = SimpleQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    sq.display()
    
    sq.dequeue()
    sq.display()
