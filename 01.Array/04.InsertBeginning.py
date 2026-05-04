# Insert at beginning without using insert()

array = [1, 2, 3, 4, 5]
value = 100

new_array = []

# Step 1: add new value first
new_array += [value]

# Step 2: copy old elements
for i in array:
    new_array += [i]

print("Insert at Beginning:", new_array)

# Time Complexity: O(n)