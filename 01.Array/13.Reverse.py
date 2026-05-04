# (Reverse Operation) ==> Reverse array without using reverse()

# Step 1: Create an array
array = [1, 2, 3, 4, 5]

# Step 2: Create empty array
new_array = []

# Step 3: Traverse from last to first
for i in range(len(array) - 1, -1, -1):
    new_array += [array[i]]

# Step 4: Print reversed array
print("Reversed Array:", new_array)

# Time Complexity: O(n)
# Reason:
# Loop runs n times → copies all elements