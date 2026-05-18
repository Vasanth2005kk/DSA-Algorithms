# (Display Operation) ==> Print all elements in stack

# Step 1: Create a stack
stack = [1, 2, 3, 4, 5]

# Step 2: Loop through and print elements (often top to bottom)
print("Stack elements (top to bottom):")
for element in reversed(stack):
    print(element)

# Time Complexity:
# O(n) → Traversing all n elements in the stack

# output  --> Stack elements (top to bottom):
# output  --> 5
# output  --> 4
# output  --> 3
# output  --> 2
# output  --> 1