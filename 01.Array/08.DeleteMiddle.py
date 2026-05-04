# (Delete Middle) ==> Remove element at given index

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Index to remove (here index 2 → value = 3)
index = 2

# Step 3: Create empty array to store result
new_array = []

# Step 4: Traverse all elements
for i in range(len(array)):
    # Check if current index is NOT the one to delete
    if i != index:
        # Copy element to new_array
        new_array += [array[i]]

# Step 5: Print result after deletion
print("After Delete Middle:", new_array)

# Time Complexity: O(n)
# Reason:
# Loop runs through all elements (n times)
# Copy operation also happens for (n-1) elements
# So overall O(n)