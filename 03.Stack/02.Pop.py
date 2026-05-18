# (Pop Operation) ==> Remove top element

# Step 1: Create a stack
stack = [1, 2, 3, 4]

# Step 2: Remove top element using pop
removed_element = stack.pop()

# Step 3: Print the removed element and updated stack
print("Removed element:", removed_element)
print("Stack after pop:", stack)

# Time Complexity:
# O(1) → Removing from the end of a list is constant time

# output  --> Removed element: 4
# output  --> Stack after pop: [1, 2, 3]