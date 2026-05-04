# (Count Occurrence) ==> Count how many times a value appears

# Step 1: Original array
array = [1, 2, 3, 2, 4, 2, 5]

# Step 2: Target value
target = 2

# Step 3: Initialize counter
count = 0

# Step 4: Traverse and count
for i in array:
    if i == target:
        count += 1

# Step 5: Print result
print("Count of", target, ":", count)

# Time Complexity: O(n)
# Reason:
# Loop checks all elements