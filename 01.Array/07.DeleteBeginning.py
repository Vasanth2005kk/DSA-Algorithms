# (Delete Beginning) ==> Remove first element

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Create empty array to store result
new_array = []

# Step 3: Start loop from index 1 (skip first element at index 0)
for i in range(1, len(array)):
    # Copy each element (except first) into new_array
    new_array += [array[i]]

# Step 4: Print final array after deletion
print("After Delete Beginning:", new_array)

# Time Complexity: O(n)
# Reason:
# Loop runs (n-1) times → almost n → so O(n)