
# What is an Array?

An Array is a data structure used to store multiple values in a single variable.

### Example
Array = [1,2,3,4,5]

### Real-Life Example

|Index|0|1|2|
|------|---|---|---|
|Fruits|[🍎|🥭|🍊]|

## All Operations

| Operation            | Description             | Example                  | Time Complexity |
| -------------------- | ----------------------- | ------------------------ | --------------- |
| Access               | Get element using index | `arr[1]`                 | O(1)            |
| Traversal            | Visit all elements      | `for i in arr`           | O(n)            |
| Insert End           | Add element at end      | `arr.append(10)`         | O(1)            |
| Insert Beginning     | Add element at start    | `arr.insert(0, 10)`      | O(n)            |
| Insert Middle        | Add element in middle   | `arr.insert(2, 10)`      | O(n)            |
| Delete End           | Remove last element     | `arr.pop()`              | O(1)            |
| Delete Beginning     | Remove first element    | `arr.pop(0)`             | O(n)            |
| Delete Middle        | Remove middle element   | `arr.remove(20)`         | O(n)            |
| Update               | Change existing value   | `arr[1] = 5`             | O(1)            |
| Linear Search        | Search one by one       | `if x in arr`            | O(n)            |
| Binary Search        | Search in sorted array  | Binary Search Algorithm  | O(log n)        |
| Sort                 | Arrange elements        | `arr.sort()`             | O(n log n)      |
| Reverse              | Reverse array           | `arr.reverse()`          | O(n)            |
| Copy                 | Copy all elements       | `arr.copy()`             | O(n)            |
| Merge/Concatenate    | Combine arrays          | `arr1 + arr2`            | O(n + m)        |
| Slice                | Get part of array       | `arr[1:4]`               | O(k)            |
| Find Length          | Count elements          | `len(arr)`               | O(1)            |
| Check Element Exists | Verify value exists     | `10 in arr`              | O(n)            |
| Find Maximum         | Largest value           | `max(arr)`               | O(n)            |
| Find Minimum         | Smallest value          | `min(arr)`               | O(n)            |
| Sum of Elements      | Add all values          | `sum(arr)`               | O(n)            |
| Clear Array          | Remove all elements     | `arr.clear()`            | O(1)            |
| Resize Dynamic Array | Increase capacity       | Automatic in Python list | O(n)            |
| Iterate with Index   | Access index + value    | `enumerate(arr)`         | O(n)            |
| Count Occurrence     | Count repeated values   | `arr.count(10)`          | O(n)            |
| Find Index           | Get element position    | `arr.index(10)`          | O(n)            |



<img width="753" height="449" alt="Screenshot from 2026-05-04 16-38-08" src="https://github.com/user-attachments/assets/ea8381d9-e737-43be-8fc6-e08340d2c789" />
