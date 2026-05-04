# (Resize Dynamic Array) ==> Increase size manually

# Step 1: Original array
array = [1, 2, 3, 4]

# Step 2: New size
new_size = 8

# Step 3: Create new array with default values
new_array = [0] * new_size

# Step 4: Copy old elements
for i in range(len(array)):
    new_array[i] = array[i]

# Step 5: Print result
print("Resized Array:", new_array)

# Time Complexity: O(n)
# Reason:
# Copying all elements