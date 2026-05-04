# (Find Index) ==> Find position of element (first occurrence)

# Step 1: Original array
array = [1, 2, 3, 2, 4, 5]

# Step 2: Target value
target = 2

# Step 3: Default index (not found)
index = -1

# Step 4: Traverse array
for i in range(len(array)):
    if array[i] == target:
        index = i
        break  # stop at first occurrence

# Step 5: Print result
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")

# Time Complexity: O(n)
# Reason:
# In worst case, loop checks all elements