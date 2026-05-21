# (isFull Operation) ==> Check queue full or not (array queue)

# Step 1: Create a queue and define its maximum capacity
queue = [10, 20, 30, 40, 50]
MAX_CAPACITY = 5

# Step 2: Check if the number of elements equals MAX_CAPACITY
if len(queue) == MAX_CAPACITY:
    print("Queue is Full")
else:
    print("Queue is not Full")

# Time Complexity:
# O(1) → Checking length and comparing is constant time

# output  --> Queue is Full
