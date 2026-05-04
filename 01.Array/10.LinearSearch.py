# (Linear Search) ==> Search element one by one from start to end

# Meaning:
# Linear Search checks each element in the array sequentially
# until the target value is found or the array ends.

# Step 1: Create an array
array = [10, 20, 30, 40, 50]

# Step 2: Target value to search
target = 30

# Step 3: Assume not found
found = False

# Step 4: Traverse array
for i in range(len(array)):
    # Check if current element matches target
    if array[i] == target:
        print("Element found at index:", i)
        found = True
        break  # stop after finding

# Step 5: If not found
if not found:
    print("Element not found")

# Time Complexity: O(n)
# Reason:
# In worst case, loop checks all elements