# (Circular Queue Implementation) ==> Last position connects to first

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
        
    def is_empty(self):
        return self.front == -1
        
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
        
    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
            print(f"Enqueued: {item}")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(f"Enqueued: {item}")
            
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        elif self.front == self.rear:
            removed = self.queue[self.front]
            self.front = self.rear = -1
            print(f"Dequeued: {removed}")
            return removed
        else:
            removed = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print(f"Dequeued: {removed}")
            return removed
            
    def display(self):
        if self.is_empty():
            print("Queue is Empty")
        elif self.rear >= self.front:
            print("Queue:", self.queue[self.front:self.rear + 1])
        else:
            print("Queue:", self.queue[self.front:] + self.queue[:self.rear + 1])

# Example Usage
if __name__ == "__main__":
    print("--- Circular Queue ---")
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()
    
    cq.dequeue()
    cq.enqueue(6)  # This will wrap around and take the empty spot at the front
    cq.display()
