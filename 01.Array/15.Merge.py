# (Merge / Concatenate Operation) ==> Combine two arrays (manual)

# Step 1: Two arrays
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# Step 2: Create empty array
merged_array = []

# Step 3: Copy elements from arr1
for i in range(len(arr1)):
    merged_array += [arr1[i]]

# Step 4: Copy elements from arr2
for i in range(len(arr2)):
    merged_array += [arr2[i]]

# Step 5: Print merged array
print("Merged Array:", merged_array)

# Time Complexity: O(n + m)
# Reason:
# Traverse arr1 (n) + arr2 (m)