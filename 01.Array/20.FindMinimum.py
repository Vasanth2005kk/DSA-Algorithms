# (Find Minimum) ==> Get smallest element (manual)

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Assume first element as minimum
min_value = array[0]

# Step 3: Traverse and compare
for i in array:
    if i < min_value:
        min_value = i

# Step 4: Print result
print("Minimum Value:", min_value)

# Time Complexity: O(n)
# Reason:
# Loop checks all elements