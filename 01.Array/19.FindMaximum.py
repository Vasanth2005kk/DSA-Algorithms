# (Find Maximum) ==> Get largest element (manual)

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Assume first element as maximum
max_value = array[0]

# Step 3: Traverse and compare
for i in array:
    if i > max_value:
        max_value = i

# Step 4: Print result
print("Maximum Value:", max_value)

# Time Complexity: O(n)
# Reason:
# Loop checks all elements