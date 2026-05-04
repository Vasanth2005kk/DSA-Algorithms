# (Check Element Exists) ==> Check if value is present (manual)

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Target value
target = 3

# Step 3: Assume not found
found = False

# Step 4: Traverse and check
for i in array:
    if i == target:
        found = True
        break

# Step 5: Print result
if found:
    print("Element exists")
else:
    print("Element doesn't exist")

# Time Complexity: O(n)