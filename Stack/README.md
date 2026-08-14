# 📚 Stack Data Structure

A Python implementation of Stack data structures using both Array-based and Linked List-based approaches.

---

## 📌 Overview

A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle.

The last element inserted into the stack is the first element removed.

This module provides two implementations:

- Array Stack
- Linked List Stack

---

## 🧩 Implementation

Main files:

Stack/
- stack_Array.py
- stack_linkedlist.py
- stack_main.py

### stack_Array.py

Contains the array-based Stack implementation.

### stack_linkedlist.py

Contains the linked-list-based Stack implementation.

### stack_main.py

Provides the interactive terminal menu for Stack operations.

---

## ⚙️ Supported Operations

| Operation | Description |
|---|---|
| push() | Add an element to the top |
| pop() | Remove the top element |
| peek() | View the top element |
| display() | Display stack elements |
| is_empty() | Check whether the stack is empty |

---

## 🧠 LIFO Principle

Stack follows the LIFO principle:

10 → 20 → 30

The last element inserted, 30, is removed first.

After pop:

10 → 20

---

## ⏱️ Time Complexity

| Operation | Complexity |
|---|---:|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |
| Display | O(n) |

---

## 💾 Space Complexity

The Stack requires O(n) space for n elements.

---

## ▶️ Running the Module

From the project root:

python -m Stack.stack_main

Or run the complete project:

python app.py

Then select:

3. Stack

---

## 🎯 Educational Purpose

This module demonstrates:

- LIFO data structures
- Stack insertion
- Stack deletion
- Top element management
- Array-based implementation
- Linked-list-based implementation
- Time and space complexity

---

## 🔗 Part of the Project

This Stack implementation is part of the Data Structures Project, which also includes:

- Array
- Singly Linked List
- Doubly Linked List
- Queue
- Binary Search Tree
- Graph
- Heap
- Hash Table
- Sorting Algorithms
- Searching Algorithms
