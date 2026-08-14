# 🚶 Queue Data Structure

A Python implementation of Queue data structures using both Array-based and Linked List-based approaches.

---

## 📌 Overview

A Queue is a linear data structure that follows the FIFO (First In, First Out) principle.

The first element inserted into the queue is the first element removed.

This module provides two implementations:

- Array Queue
- Linked List Queue

---

## 🧩 Implementation

Main files:

Queue/
- queue_Array.py
- queue_linkdlist.py
- queue_main.py

### queue_Array.py

Contains the array-based Queue implementation.

### queue_linkdlist.py

Contains the linked-list-based Queue implementation.

### queue_main.py

Provides the interactive terminal menu for Queue operations.

---

## ⚙️ Supported Operations

| Operation | Description |
|---|---|
| Enequeue() | Add an element to the rear |
| dequeue() | Remove the front element |
| get_fron() | Get the front element |
| get_rear() | Get the rear element |
| getFront() | Get the front element in Linked Queue |
| getRear() | Get the rear element in Linked Queue |
| Dequeue() | Remove the front element from Linked Queue |

---

## 🧠 FIFO Principle

Queue follows the FIFO principle:

10 → 20 → 30

The first element inserted is the first element removed.

After removing 10:

20 → 30

---

## ⏱️ Time Complexity

| Operation | Complexity |
|---|---:|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Get Front | O(1) |
| Get Rear | O(1) |
| Search | O(n) |

---

## 💾 Space Complexity

The Queue requires O(n) space for n elements.

---

## ▶️ Running the Module

From the project root:

python -m Queue.queue_main

Or run the complete project:

python app.py

Then select:

4. Queue

---

## 🎯 Educational Purpose

This module demonstrates:

- FIFO data structures
- Queue insertion
- Queue deletion
- Front and rear management
- Array-based implementation
- Linked-list-based implementation
- Time and space complexity

---

## 🔗 Part of the Project

This Queue implementation is part of the Data Structures Project, which also includes:

- Array
- Singly Linked List
- Doubly Linked List
- Stack
- Binary Search Tree
- Graph
- Heap
- Hash Table
- Sorting Algorithms
- Searching Algorithms
