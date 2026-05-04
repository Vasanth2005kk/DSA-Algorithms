# (Slice Operation) ==> Get part of array (manual)

# Step 1: Original array
array = [1, 2, 3, 4, 5]

# Step 2: Define slice range
start = 1
end = 4   # end is not included

# Step 3: Create empty array
sliced_array = []

# Step 4: Copy elements from start to end-1
i = start
while i < end:
    sliced_array += [array[i]]
    i += 1

# Step 5: Print result
print("Sliced Array:", sliced_array)

# Time Complexity: O(k)
# k = number of elements copied