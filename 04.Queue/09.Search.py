# (Search Operation) ==> Find element

# Step 1: Create a queue
queue = [10, 20, 30, 40, 50]

# Step 2: Define value to search
target = 30

# Step 3: Loop through to find the element
found = False
for i in range(len(queue)):
    if queue[i] == target:
        print(f"Element {target} found at position {i+1} (index {i})")
        found = True
        break

if not found:
    print(f"Element {target} not found in the queue")

# Time Complexity:
# O(n) → In the worst case, searching takes linear time

# output  --> Element 30 found at position 3 (index 2)
