# (isFull Operation) ==> Check if stack is full (for array implementation with limit)

# Step 1: Create a stack and define maximum capacity
stack = [1, 2, 3, 4]
max_capacity = 4

# Step 2: Check if stack length equals maximum capacity
if len(stack) == max_capacity:
    is_full = True
else:
    is_full = False

# Step 3: Print the result
print("Is stack full?", is_full)

# Time Complexity:
# O(1) → len() function and comparison is constant time

# output  --> Is stack full? True
