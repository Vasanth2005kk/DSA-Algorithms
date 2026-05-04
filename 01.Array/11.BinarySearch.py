# (Binary Search) ==> Search element using divide and conquer (sorted array only)

# Meaning:
# Binary Search finds the target by repeatedly dividing the array into halves.
# It works only on sorted arrays.

# Step 1: Create a sorted array
array = [10, 20, 30, 40, 50]

# Step 2: Target value to search
target = 30

# Step 3: Initialize pointers
left = 0
right = len(array) - 1

# Step 4: Perform search
found = False

while left <= right:
    # Find middle index
    mid = (left + right) // 2

    # Check if middle element is target
    if array[mid] == target:
        print("Element found at index:", mid)
        found = True
        break

    # If target is greater, search right half
    elif array[mid] < target:
        left = mid + 1

    # If target is smaller, search left half
    else:
        right = mid - 1

# Step 5: If not found
if not found:
    print("Element not found")

# Time Complexity: O(log n)
# Reason:
# Each step reduces search space by half