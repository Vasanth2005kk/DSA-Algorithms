# 📦 Arrays — Data Structure Guide

> An **Array** is one of the most fundamental data structures in programming.  
> It stores **multiple values in a single variable**, all in a sequential (ordered) manner.

---

## 🤔 What is an Array?

Imagine a **row of boxes**, each labeled with a number (index) starting from `0`.  
Each box holds one value. You can directly open any box using its label.

```
Index →   0    1    2    3    4
        ┌────┬────┬────┬────┬────┐
Array → │ 10 │ 20 │ 30 │ 40 │ 50 │
        └────┴────┴────┴────┴────┘
```

```python
# Creating an array in Python
array = [10, 20, 30, 40, 50]
```
<p align="center">
  <img width="800" height="449" alt="Array Visualization" src="https://github.com/user-attachments/assets/ea8381d9-e737-43be-8fc6-e08340d2c789" />
</p>

## 🍎 Real-Life Example

Think of a **fruit basket with numbered slots**:

| Index | 0  | 1  | 2  |
|-------|----|----|-----|
| Fruit | 🍎 | 🥭 | 🍊 |

- Slot `0` → Apple 🍎  
- Slot `1` → Mango 🥭  
- Slot `2` → Orange 🍊  

You can **directly pick** the fruit at any slot using its number — that's how arrays work!

---

## 🧠 Key Concepts to Remember

| Concept | Explanation |
|---------|-------------|
| **Index** | Position of element, starts from `0` |
| **Element** | Value stored at a position |
| **Length** | Total number of elements |
| **0-based indexing** | First element is at index `0`, not `1` |

```python
array = [10, 20, 30, 40, 50]
#         ↑               ↑
#      index 0         index 4  (length = 5)
```

---

## ⚡ Why Use Arrays?

- ✅ **Fast access** — Get any element instantly using index `O(1)`
- ✅ **Simple structure** — Easy to understand and use
- ✅ **Memory efficient** — Elements stored in contiguous memory
- ✅ **Versatile** — Supports many operations (search, sort, slice, etc.)

---

## 📂 Files in This Folder

Each operation has its own Python file with step-by-step code and comments:

| # | File | Operation | What it does |
|---|------|-----------|--------------|
| 01 | [01.Access.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/01.Access.py) | Access | Get element by index |
| 02 | [02Traversal.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/02Traversal.py) | Traversal | Visit every element |
| 03 | [03.InsertEnd.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/03.InsertEnd.py) | Insert End | Add element at end |
| 04 | [04.InsertBeginning.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/04.InsertBeginning.py) | Insert Beginning | Add element at start |
| 05 | [05.InsertMiddle.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/05.InsertMiddle.py) | Insert Middle | Add element at any position |
| 06 | [06.DeleteEnd.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/06.DeleteEnd.py) | Delete End | Remove last element |
| 07 | [07.DeleteBeginning.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/07.DeleteBeginning.py) | Delete Beginning | Remove first element |
| 08 | [08.DeleteMiddle.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/08.DeleteMiddle.py) | Delete Middle | Remove element at position |
| 09 | [09.Update.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/09.Update.py) | Update | Change value at index |
| 10 | [10.LinearSearch.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/10.LinearSearch.py) | Linear Search | Search one by one |
| 11 | [11.BinarySearch.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/11.BinarySearch.py) | Binary Search | Fast search (sorted array) |
| 12 | [12.Sort.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/12.Sort.py) | Sort | Arrange in order |
| 13 | [13.Reverse.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/13.Reverse.py) | Reverse | Flip the array |
| 14 | [14.Copy.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/14.Copy.py) | Copy | Duplicate the array |
| 15 | [15.Merge.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/15.Merge.py) | Merge | Combine two arrays |
| 16 | [16.Slice.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/16.Slice.py) | Slice | Extract a part |
| 17 | [17.FindLength.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/17.FindLength.py) | Find Length | Count elements |
| 18 | [18.CheckElementExists.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/18.CheckElementExists.py) | Check Exists | Is value in array? |
| 19 | [19.FindMaximum.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/19.FindMaximum.py) | Find Maximum | Largest value |
| 20 | [20.FindMinimum.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/20.FindMinimum.py) | Find Minimum | Smallest value |
| 21 | [21.SumofElements.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/21.SumofElements.py) | Sum | Add all values |
| 22 | [22.ClearArray.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/22.ClearArray.py) | Clear | Remove all elements |
| 23 | [23.ResizeDynamicArray.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/23.ResizeDynamicArray.py) | Resize | Expand array capacity |
| 24 | [24.IteratewithIndex.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/24.IteratewithIndex.py) | Iterate with Index | Loop with index + value |
| 25 | [25.CountOccurrence.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/25.CountOccurrence.py) | Count Occurrence | How many times value appears |
| 26 | [26.FindIndex.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/01.Array/26.FindIndex.py) | Find Index | Get position of a value |

---

## 🔧 All Operations — Quick Reference

| Operation | Description | Python Example | Time Complexity |
|-----------|-------------|----------------|-----------------|
| **Access** | Get element using index | `arr[1]` | O(1) |
| **Traversal** | Visit all elements | `for i in arr` | O(n) |
| **Insert End** | Add element at end | `arr.append(10)` | O(1) |
| **Insert Beginning** | Add element at start | `arr.insert(0, 10)` | O(n) |
| **Insert Middle** | Add element in middle | `arr.insert(2, 10)` | O(n) |
| **Delete End** | Remove last element | `arr.pop()` | O(1) |
| **Delete Beginning** | Remove first element | `arr.pop(0)` | O(n) |
| **Delete Middle** | Remove middle element | `arr.remove(20)` | O(n) |
| **Update** | Change existing value | `arr[1] = 5` | O(1) |
| **Linear Search** | Search one by one | `if x in arr` | O(n) |
| **Binary Search** | Search in sorted array | Binary Search Algorithm | O(log n) |
| **Sort** | Arrange elements | `arr.sort()` | O(n log n) |
| **Reverse** | Reverse array | `arr.reverse()` | O(n) |
| **Copy** | Copy all elements | `arr.copy()` | O(n) |
| **Merge / Concatenate** | Combine arrays | `arr1 + arr2` | O(n + m) |
| **Slice** | Get part of array | `arr[1:4]` | O(k) |
| **Find Length** | Count elements | `len(arr)` | O(1) |
| **Check Element Exists** | Verify value exists | `10 in arr` | O(n) |
| **Find Maximum** | Largest value | `max(arr)` | O(n) |
| **Find Minimum** | Smallest value | `min(arr)` | O(n) |
| **Sum of Elements** | Add all values | `sum(arr)` | O(n) |
| **Clear Array** | Remove all elements | `arr.clear()` | O(1) |
| **Resize Dynamic Array** | Increase capacity | Automatic in Python list | O(n) |
| **Iterate with Index** | Access index + value | `enumerate(arr)` | O(n) |
| **Count Occurrence** | Count repeated values | `arr.count(10)` | O(n) |
| **Find Index** | Get element position | `arr.index(10)` | O(n) |

---

## ⏱️ Time Complexity — Explained Simply

| Complexity | Meaning | Feel |
|------------|---------|------|
| **O(1)** | Constant time — instant | ⚡ Super fast |
| **O(log n)** | Cuts problem in half each step | 🚀 Very fast |
| **O(n)** | Loops through all elements | 🔄 Linear |
| **O(n log n)** | Loop + smart splitting | 📊 Efficient sort |
| **O(n + m)** | Depends on both array sizes | 🔗 For merge ops |
| **O(k)** | Depends on slice size `k` | ✂️ For slice ops |

---

## 💡 Quick Tips

- 🔢 **Indexing starts at 0** — `array[0]` is the first element
- 🔁 **Use `for i in array`** to simply loop through values
- 📌 **Use `enumerate(array)`** when you need both index and value
- 🔍 **Binary Search** only works on **sorted arrays**
- 🐍 **Python lists** are dynamic arrays — they resize automatically
- ➕ **`append()`** is faster than `insert(0, value)` — O(1) vs O(n)

---

## 🧪 Quick Example

```python
# A complete mini demo of array operations
array = [5, 3, 1, 4, 2]

# Sort
array.sort()
print("Sorted:", array)         # [1, 2, 3, 4, 5]

# Access
print("First:", array[0])       # 1

# Search
print("Index of 3:", array.index(3))  # 2

# Insert
array.append(6)
print("After Insert:", array)   # [1, 2, 3, 4, 5, 6]

# Delete
array.pop()
print("After Delete:", array)   # [1, 2, 3, 4, 5]

# Length
print("Length:", len(array))    # 5
```
