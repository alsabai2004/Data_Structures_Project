# 📦 Array Data Structure

A Python implementation of an Array data structure with common element-management and searching operations.

---

## 📌 Overview

The `Arrays` class provides a simple interface for creating and manipulating a collection of elements.

The implementation supports:

- Creating an array with a specified size
- Inserting elements
- Displaying elements
- Deleting one occurrence
- Deleting all occurrences
- Keeping the first occurrence
- Searching for elements
- Getting the array length
- Checking whether the array is empty
- Clearing the array
- Accessing an element by index

---

## 🧩 Implementation

The main implementation is located in:

Array/
- array.py
- array_main.py

### array.py

Contains the `Arrays` class and its core operations.

### array_main.py

Provides an interactive terminal menu for working with the Array implementation.

---

## ⚙️ Supported Operations

| Operation | Description |
|---|---|
| `insert()` | Insert elements into the array |
| `display()` | Display all elements |
| `deleteitem()` | Delete the first matching element |
| `deleteALLItem()` | Delete all occurrences of an element |
| `notfirst()` | Delete duplicates while keeping the first occurrence |
| `search()` | Search for an element |
| `get_length()` | Return the number of elements |
| `is_empty()` | Check whether the array is empty |
| `clear()` | Remove all elements |
| `get()` | Access an element by index |

---

## 🧠 Example

    from Array.array import Arrays

    arr = Arrays(5)

    arr.data = [10, 20, 30, 40, 50]
    arr.size = len(arr.data)

    print(arr.search(30))
    print(arr.get(2))

    arr.deleteitem(30)

    print(arr)

Output:

    True
    30
    [10, 20, 40, 50]

---

## ⏱️ Time Complexity

| Operation | Complexity |
|---|---:|
| Access by index | `O(1)` |
| Search | `O(n)` |
| Insert | `O(n)` |
| Delete one item | `O(n)` |
| Delete all occurrences | `O(n)` |
| Get length | `O(1)` |
| Check empty | `O(1)` |
| Clear | `O(n)` |

> Complexity depends on the underlying Python list operations used by the implementation.

---

## 💾 Space Complexity

The Array uses `O(n)` storage for `n` elements.

---

## ▶️ Running the Module

From the project root:

    python -m Array.array_main

Or run the complete project:

    python app.py

Then select:

    1. Array

---

## 🛡️ Validation

The implementation validates:

- Negative array sizes
- Invalid integer input
- Invalid indexes
- Missing elements

---

## 🎯 Educational Purpose

This module demonstrates fundamental Array concepts and provides practical experience with:

- Sequential data storage
- Index-based access
- Searching
- Element deletion
- Data manipulation
- Complexity analysis

---

## 🔗 Part of the Project

This module is part of the Data Structures Project, which also includes:

- Linked Lists
- Stack
- Queue
- Binary Search Tree
- Graph
- Heap
- Hash Table
- Sorting Algorithms
- Searching Algorithms
