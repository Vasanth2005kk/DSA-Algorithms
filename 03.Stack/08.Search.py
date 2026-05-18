# (Search Operation) ==> Find an element in the stack

# Step 1: Create a stack and value to search
stack = [10, 20, 30, 40, 50]
value_to_search = 30

# Step 2: Search for the value (usually 1-based index from top in classic stack)
# Here we'll find if it exists and its position from the top
position = -1
for i in range(len(stack) - 1, -1, -1):
    if stack[i] == value_to_search:
        position = len(stack) - i
        break

# Step 3: Print the result
if position != -1:
    print(f"Element {value_to_search} found at position {position} from top.")
else:
    print(f"Element {value_to_search} not found in stack.")

# Time Complexity:
# O(n) → May need to traverse all elements to find the value

# output  --> Element 30 found at position 3 from top.