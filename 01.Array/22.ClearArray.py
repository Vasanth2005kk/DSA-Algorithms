# (Clear Array) ==> Remove all elements (manual)

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Create empty array
new_array = []

# Step 3: Replace old array reference
array = new_array

# Step 4: Print result
print("Cleared Array:", array)

# Time Complexity: O(1)
# Reason:
# Just reassigning reference (no traversal)