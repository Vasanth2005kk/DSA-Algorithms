# (Front / Peek Operation) ==> View front element

# Step 1: Create a queue
queue = [10, 20, 30, 40]

# Step 2: View the first element without removing it
if len(queue) > 0:
    front_element = queue[0]
    print("Front element is:", front_element)
else:
    print("Queue is empty!")

# Time Complexity:
# O(1) → Accessing an element by index in a list is constant time

# output  --> Front element is: 10
