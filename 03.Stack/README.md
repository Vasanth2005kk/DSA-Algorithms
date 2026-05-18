# 🥞 Stacks — Data Structure Guide

> A **Stack** is a linear data structure that follows a particular order in which operations are performed.
> The order is **LIFO (Last In First Out)** or **FILO (First In Last Out)**.

---

## 🤔 What is a Stack?

Imagine a **stack of plates** in a cafeteria.  
You can only add a new plate to the top, and you can only remove the top plate. 
The last plate you put on the stack will be the first one you take off.

```
Top →  ┌────┐
       │ 40 │
       ├────┤
       │ 30 │
       ├────┤
       │ 20 │
       ├────┤
       │ 10 │
       └────┘
       Bottom
```

```python
# Creating a stack using a list in Python
stack = [10, 20, 30, 40]
```

## 🍎 Real-Life Example

Think of the **Undo feature** in your text editor:

- Action 1: Type "Hello"
- Action 2: Type "World"
- Action 3: Make it bold

When you press Undo (Ctrl+Z):
- **First undo** removes "Make it bold" (Last action)
- **Second undo** removes "World"
- **Third undo** removes "Hello"

You are retrieving operations in the exact reverse order of how you made them!

---

## 🧠 Key Concepts to Remember

| Concept | Explanation |
|---------|-------------|
| **Push** | Adding an element to the top of the stack |
| **Pop** | Removing an element from the top of the stack |
| **Peek / Top** | Looking at the top element without removing it |
| **LIFO** | Last In First Out principle |

---

## ⚡ Why Use Stacks?

- ✅ **Fast operations** — Add or remove at the top instantly `O(1)`
- ✅ **Undo/Redo** — Perfect for reversing actions or traversing back
- ✅ **Function Calls** — Used by computers to manage function calls (Call Stack)
- ✅ **Expression Evaluation** — Used in validating parenthesis and calculating expressions

---

## 📂 Files in This Folder

Each operation has its own Python file with step-by-step code and comments:

| # | File | Operation | What it does |
|---|------|-----------|--------------|
| 01 | [01.Push.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/01.Push.py) | Push | Add element to top |
| 02 | [02.Pop.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/02.Pop.py) | Pop | Remove top element |
| 03 | [03.Peek.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/03.Peek.py) | Peek / Top | View top element |
| 04 | [04.isEmpty.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/04.isEmpty.py) | isEmpty | Check stack empty or not |
| 05 | [05.isFull.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/05.isFull.py) | isFull | Check stack full or not (array stack) |
| 06 | [06.Size.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/06.Size.py) | Size | Get number of elements |
| 07 | [07.Display.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/07.Display.py) | Display | Print all elements |
| 08 | [08.Search.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/03.Stack/08.Search.py) | Search | Find an element |

---

## 🔧 All Operations — Quick Reference

| Operation | Description | Python Example | Time Complexity |
|-----------|-------------|----------------|-----------------|
| **Push** | Add element to top | `stack.append(10)` | O(1) |
| **Pop** | Remove top element | `stack.pop()` | O(1) |
| **Peek / Top** | View top element | `stack[-1]` | O(1) |
| **isEmpty** | Check stack empty or not | `len(stack) == 0` | O(1) |
| **isFull** | Check stack full or not | `len(stack) == MAX` | O(1) |
| **Size** | Get number of elements | `len(stack)` | O(1) |
| **Display** | Print all elements | `for i in reversed(stack)` | O(n) |
| **Search** | Find an element | Loop to find value | O(n) |

---

## ⏱️ Time Complexity — Explained Simply

| Complexity | Meaning | Feel |
|------------|---------|------|
| **O(1)** | Constant time — instant | ⚡ Super fast |
| **O(n)** | Loops through elements | 🔄 Linear |

---

## 💡 Quick Tips

- 📚 Python `list` acts as a great Stack because `append()` and `pop()` are already `O(1)`.
- ⚠️ If you use `insert(0, val)` or `pop(0)` on a list, it becomes `O(n)` which is bad for a stack. Always add/remove from the end!
- ⚡ For multi-threading, `collections.deque` is a faster alternative for stacks in Python.

---

## 🧪 Quick Example

```python
# A complete mini demo of stack operations
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)
print("After Push:", stack)    # [10, 20, 30]

# Peek
print("Top Element:", stack[-1]) # 30

# Pop
stack.pop()
print("After Pop:", stack)     # [10, 20]

# Size
print("Stack Size:", len(stack)) # 2
```
