# (Rear Operation) ==> View last element

# Step 1: Create a queue
queue = [10, 20, 30, 40]

# Step 2: View the last element without removing it
if len(queue) > 0:
    rear_element = queue[-1]
    print("Rear element is:", rear_element)
else:
    print("Queue is empty!")

# Time Complexity:
# O(1) → Accessing the last element in a list is constant time

# output  --> Rear element is: 40
