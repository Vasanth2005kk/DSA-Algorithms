# 🚶 Queues — Data Structure Guide

> A **Queue** is a linear data structure that follows a particular order in which operations are performed.
> The order is **FIFO (First In First Out)**.

---

## 🤔 What is a Queue?

Imagine a **line of people** waiting for a movie ticket.  
The first person to join the line is the first one to get the ticket and leave. 
The last person to join the line will be the last one to be served.

```text
Front →  ┌────┐
         │ 10 │
         ├────┤
         │ 20 │
         ├────┤
         │ 30 │
         ├────┤
         │ 40 │
         └────┘
         Rear
```

```python
# Creating a queue using a list in Python
queue = [10, 20, 30, 40]
```

## 🍎 Real-Life Example

Think of a **printer queue**:

- Action 1: Send Document A to print
- Action 2: Send Document B to print
- Action 3: Send Document C to print

When the printer starts:
- **First**, Document A gets printed (First in, first out)
- **Second**, Document B gets printed
- **Third**, Document C gets printed

The printer processes tasks in the exact order they were received!

---

## 🧠 Key Concepts to Remember

| Concept | Explanation |
|---------|-------------|
| **Enqueue** | Adding an element to the rear of the queue |
| **Dequeue** | Removing an element from the front of the queue |
| **Front / Peek** | Looking at the first element without removing it |
| **Rear** | Looking at the last element |
| **FIFO** | First In First Out principle |

---

## ⚡ Why Use Queues?

- ✅ **Order Preservation** — Tasks are processed in the exact order they arrive.
- ✅ **Scheduling** — Operating systems use queues for CPU and disk scheduling.
- ✅ **Asynchronous Data Transfer** — Used in IO Buffers, pipes, file IO, etc.
- ✅ **Breadth-First Search (BFS)** — Essential for graph traversal algorithms.

---

## 🏷️ Types of Queues

| Queue Type                 | Description                     |
| -------------------------- | ------------------------------- |
| **Simple Queue**           | Normal FIFO queue               |
| **Circular Queue**         | Last position connects to first |
| **Priority Queue**         | Higher priority removed first   |
| **Double Ended Queue (Deque)** | Insert/Delete both ends         |

---

## 📂 Files in This Folder

Each operation has its own Python file with step-by-step code and comments:

| # | File | Operation | What it does |
|---|------|-----------|--------------|
| 01 | [01.Enqueue.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/01.Enqueue.py) | Enqueue | Add element at rear |
| 02 | [02.Dequeue.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/02.Dequeue.py) | Dequeue | Remove element from front |
| 03 | [03.Front.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/03.Front.py) | Front / Peek | View front element |
| 04 | [04.Rear.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/04.Rear.py) | Rear | View last element |
| 05 | [05.isEmpty.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/05.isEmpty.py) | isEmpty | Check queue empty or not |
| 06 | [06.isFull.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/06.isFull.py) | isFull | Check queue full or not |
| 07 | [07.Size.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/07.Size.py) | Size | Count elements |
| 08 | [08.Display.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/08.Display.py) | Display | Print all elements |
| 09 | [09.Search.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/09.Search.py) | Search | Find element |
| 10 | [10.Simple_Queue.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/10.Simple_Queue.py) | Class Impl | Simple Queue class example |
| 11 | [11.Circular_Queue.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/11.Circular_Queue.py) | Class Impl | Circular Queue implementation |
| 12 | [12.Priority_Queue.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/12.Priority_Queue.py) | Class Impl | Priority Queue implementation |
| 13 | [13.Deque.py](https://github.com/Vasanth2005kk/DSA-Algorithms/blob/main/04.Queue/13.Deque.py) | Class Impl | Double Ended Queue implementation |

---

## 🔧 All Operations — Quick Reference

| Operation | Description | Python Example | Time Complexity |
|-----------|-------------|----------------|-----------------|
| **Enqueue** | Add element at rear | `queue.append(10)` | O(1) |
| **Dequeue** | Remove element from front | `queue.pop(0)` | O(n) |
| **Front / Peek** | View front element | `queue[0]` | O(1) |
| **Rear** | View last element | `queue[-1]` | O(1) |
| **isEmpty** | Check queue empty or not | `len(queue) == 0` | O(1) |
| **isFull** | Check queue full or not | `len(queue) == MAX` | O(1) |
| **Size** | Count elements | `len(queue)` | O(1) |
| **Display** | Print all elements | `for val in queue:` | O(n) |
| **Search** | Find element | Loop to find value | O(n) |

*(Note: While `pop(0)` is `O(n)` on a list, using `collections.deque` makes both `append()` and `popleft()` `O(1)`)*

---

## ⏱️ Time Complexity — Explained Simply

| Complexity | Meaning | Feel |
|------------|---------|------|
| **O(1)** | Constant time — instant | ⚡ Super fast |
| **O(n)** | Loops through elements | 🔄 Linear |

---

## 💡 Quick Tips

- 📚 Python `list` is okay for simple queues, but `pop(0)` shifts all elements, which is slow `O(n)`.
- ⚡ **Pro Tip:** Use `collections.deque` in Python for real queues! It makes `append()` and `popleft()` both incredibly fast `O(1)`.
- 🔄 Queues are often used to implement Breadth-First Search (BFS) in trees and graphs!

---

## 🧪 Quick Example

```python
# A complete mini demo of queue operations using a list
queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)
print("After Enqueue:", queue)    # [10, 20, 30]

# Front
print("Front Element:", queue[0]) # 10

# Dequeue
queue.pop(0)
print("After Dequeue:", queue)     # [20, 30]

# Size
print("Queue Size:", len(queue))   # 2
```
