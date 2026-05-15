# 🔗 Linked List — Data Structure Guide

> A **Linked List** is a linear data structure where elements are not stored in contiguous memory locations.  
> Instead, each element (called a **Node**) is a separate object that contains a **value** and a **reference (pointer)** to the next node in the sequence.

---

## 🤔 What is a Linked List?

Imagine a **scavenger hunt**: each clue tells you where the next clue is hidden. You don't know where all the clues are at once; you have to follow them one by one.  
In a Linked List, every "box" (Node) knows its own value and the address of the next box.

```
         Head                                              Tail
          ↓                                                 ↓
    ┌────┬────┐       ┌────┬────┐       ┌────┬────┐       ┌────┬────┐
    │ 10 │ ●──┼─────→ │ 20 │ ●──┼─────→ │ 30 │ ●──┼─────→ │ 40 │None│
    └────┴────┘       └────┴────┘       └────┴────┘       └────┴────┘
```

```python
# Basic structure of a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## 🍎 Real-Life Example

Think of a **Train**:

| Part | Description |
|------|-------------|
| **Engine** | The **Head** of the list |
| **Bogie** | A **Node** containing passengers (data) |
| **Coupling** | The **Pointer** (next) connecting bogies |
| **Last Bogie** | The **Tail** pointing to nothing (None) |

- To reach the 5th bogie, you **must walk through** bogies 1, 2, 3, and 4. You can't just teleport there!

---

## 🧠 Key Concepts to Remember

| Concept | Explanation |
|---------|-------------|
| **Node** | The basic unit (contains Data + Next pointer) |
| **Head** | The very first node in the list |
| **Tail** | The last node (its `next` is `None`) |
| **Pointer** | A reference to another node's memory address |

```python
node1 = Node(10)
node2 = Node(20)
node1.next = node2  # node1 points to node2
```

---

## ⚡ Why Use Linked Lists?

- ✅ **Dynamic Size** — Grows and shrinks during execution (no fixed size)
- ✅ **Fast Insertion/Deletion** — No need to "shift" elements like in arrays `O(1)` at start
- ✅ **Memory Efficient** — Uses only as much memory as needed
- ✅ **Easy Reorganization** — Just change pointers to reorder

---

## 📂 Files in This Folder

Each operation has its own Python file with step-by-step code and comments:

| # | File | Operation | What it does |
|---|------|-----------|--------------|
| 01 | [01.Create.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/01.Create.py) | Create | Initialize a new list |
| 02 | [02.Display.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/02.Display.py) | Traversal | Print all nodes in list |
| 03 | [03.InsertatBeginning.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/03.InsertatBeginning.py) | Insert Start | Add node at the beginning |
| 04 | [04.InsertatEnd.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/04.InsertatEnd.py) | Insert End | Add node at the very end |
| 05 | [05.InsertatPosition.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/05.InsertatPosition.py) | Insert Middle | Add node at specific index |
| 06 | [06.DeleteatBeginning.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/06.DeleteatBeginning.py) | Delete Start | Remove the first node |
| 07 | [07.DeleteatEnd.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/07.DeleteatEnd.py) | Delete End | Remove the last node |
| 08 | [08.DeleteatPosition.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/08.DeleteatPosition.py) | Delete Middle | Remove node at position |
| 09 | [09.Search.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/09.Search.py) | Search | Find if value exists |
| 10 | [10.Update.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/10.Update.py) | Update | Change value of a node |
| 11 | [11.Length.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/11.Length.py) | Count/Length | Get total number of nodes |
| 12 | [12.Reverse.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/12.Reverse.py) | Reverse | Flip the entire list |
| 13 | [13.Sort.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/13.Sort.py) | Sort | Arrange nodes in order |
| 14 | [14.Merge.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/14.Merge.py) | Merge | Combine two lists |
| 15 | [15.Split.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/15.Split.py) | Split | Divide list into two |
| 16 | [16.FindMiddleNode.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/16.FindMiddleNode.py) | Middle Node | Get the center node |
| 17 | [17.DetectLoop.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/17.DetectLoop.py) | Detect Loop | Check for cycles |
| 18 | [18.RemoveDuplicates.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/18.RemoveDuplicates.py) | Unique Nodes | Remove repeated values |
| 19 | [19.GetFirstNode.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/19.GetFirstNode.py) | Get Head | Access first element |
| 20 | [20.GetLastNode.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/02.Linked-List/20.GetLastNode.py) | Get Tail | Access last element |

---

## 🔧 All Operations — Quick Reference

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| **Access** | Get element at index | O(n) |
| **Search** | Find element by value | O(n) |
| **Insert Start** | Add at the beginning | O(1) |
| **Insert End** | Add at the end | O(n) (O(1) if Tail is known) |
| **Insert Middle** | Add at specific position | O(n) |
| **Delete Start** | Remove from beginning | O(1) |
| **Delete End** | Remove from end | O(n) |
| **Delete Middle** | Remove from position | O(n) |
| **Traversal** | Visit all nodes | O(n) |

---

## ⏱️ Time Complexity — Explained Simply

| Complexity | Meaning | Feel |
|------------|---------|------|
| **O(1)** | Constant time — instant | ⚡ Super fast |
| **O(n)** | Loops through nodes one by one | 🔄 Linear |
| **O(n²)** | Nested loops (often in simple sorts) | 🐌 Slower |

---

## 💡 Quick Tips

- 📍 **Always track the Head** — If you lose the head, you lose the whole list!
- 🔀 **Pointers are everything** — Be careful with the order of changing `next` references.
- 🏁 **Check for `None`** — Always check if `node.next` is None to avoid errors.
- 🚀 **Insertion at Start** is the biggest advantage over Arrays (O(1) vs O(n)).

---

## 🧪 Quick Example

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. Create Nodes
head = Node(10)
second = Node(20)
third = Node(30)

# 2. Link them
head.next = second
second.next = third

# 3. Traverse/Print
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
# Output: 10 -> 20 -> 30 -> None
```
