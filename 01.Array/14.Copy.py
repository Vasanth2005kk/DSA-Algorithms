# (Copy Operation) ==> Copy all elements to a new array (manual)

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Create empty array
new_array = []

# Step 3: Copy elements one by one
for i in range(len(array)):
    new_array += [array[i]]

# Step 4: Print copied array
print("Original Array:", array)
print("Copied Array:", new_array)

# Time Complexity: O(n)
# Reason:
# Loop runs for all elements → n times