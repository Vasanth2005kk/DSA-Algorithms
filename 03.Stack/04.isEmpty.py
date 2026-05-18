# (isEmpty Operation) ==> Check if stack is empty

# Step 1: Create an empty stack
stack = []

# Step 2: Check if stack is empty
if not stack:
    is_empty = True
else:
    is_empty = False

# Step 3: Print the result
print("Is stack empty?", is_empty)

# Time Complexity:
# O(1) → Checking boolean value of list is constant time

# output  --> Is stack empty? True
