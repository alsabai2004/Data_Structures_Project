# 🏔️ Heap Data Structure

A Python implementation of a Min Heap data structure.

---

## 📌 Overview

A Heap is a specialized tree-based data structure that satisfies the heap property.

This module implements a Min Heap, where the smallest element is always located at the root.

The implementation uses a Python list to represent the complete binary tree.

---

## 🧩 Implementation

Main files:

Heap/
- min_heap.py

---

## ⚙️ Supported Operations

| Operation | Description |
|---|---|
| insert() | Add an element to the heap |
| extract_min() | Remove and return the smallest element |
| peek() | Return the smallest element without removing it |
| heapify_up() | Restore heap property after insertion |
| heapify_down() | Restore heap property after deletion |
| is_empty() | Check whether the heap is empty |
| size() | Return the number of elements |
| display() | Display heap elements |

---

## 🧠 Min Heap Property

In a Min Heap:

The value of every parent node is less than or equal to the values of its children.

Example:

        10
       /  \
      20   30
     /  \
    40   50

The minimum value is always at the root.

---

## 📐 Array Representation

For an element at index i:

Parent index:

(i - 1) // 2

Left child:

2 * i + 1

Right child:

2 * i + 2

This allows the complete binary tree to be stored efficiently without explicit tree nodes.

---

## 🔄 Heap Operations

### Insert

A new element is added at the end of the heap.

Heapify-up then moves the element upward until the Min Heap property is restored.

### Extract Minimum

The root element is removed.

The last element replaces the root, followed by heapify-down to restore the heap property.

### Peek

Returns the minimum element without modifying the heap.

---

## ⏱️ Time Complexity

| Operation | Complexity |
|---|---:|
| Insert | O(log n) |
| Extract Minimum | O(log n) |
| Peek | O(1) |
| Heapify Up | O(log n) |
| Heapify Down | O(log n) |
| Size | O(1) |
| Is Empty | O(1) |

---

## 💾 Space Complexity

The heap requires:

O(n)

space for n elements.

---

## ▶️ Running

From the project root:

python Heap/min_heap.py

Or run the complete project:

python app.py

---

## 🎯 Educational Purpose

This module demonstrates:

- Heap data structures
- Complete binary trees
- Min Heap property
- Heap insertion
- Minimum extraction
- Heapify operations
- Array-based tree representation
- Time and space complexity

---

## 🔗 Part of the Project

This Heap implementation is part of the Data Structures Project, which also includes:

- Array
- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Binary Search Tree
- Graph
- Hash Table
- Sorting Algorithms
- Searching Algorithms
