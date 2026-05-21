# (Dequeue Operation) ==> Remove element from front manually in O(1) time

# Step 1: Create a queue and a pointer to track the front
queue = [1, 2, 3, 4, 5]
front_pointer = 0

# Step 2: Check if queue is not empty (by comparing pointer to length)
if front_pointer < len(queue):
    # Step 3: Access the front element and increment the pointer
    removed_element = queue[front_pointer]
    # Replace it with None to visually show it's removed and free memory
    queue[front_pointer] = None 
    front_pointer += 1
    
    print("Dequeued element:", removed_element)
else:
    print("Queue is empty!")

# Step 4: Print the current state of the queue
print("Actual list in memory:", queue)
print("Active queue elements:", queue[front_pointer:])

# Time Complexity:
# O(1) → Accessing by index and incrementing a pointer takes constant time!

# output  --> Dequeued element: 1
# output  --> Actual list in memory: [None, 2, 3, 4, 5]
# output  --> Active queue elements: [2, 3, 4, 5]
