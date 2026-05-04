# Insert at middle without using insert()

array = [1, 2, 3, 4, 5]
value = 100
index = 2

new_array = []
i = 0

for element in array:
    if i == index:
        new_array += [value]
    new_array += [element]
    i += 1

print("Insert at Middle:", new_array)

# Time Complexity: O(n)