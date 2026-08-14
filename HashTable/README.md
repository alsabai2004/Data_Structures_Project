# #️⃣ Hash Table Data Structure

A Python implementation of a Hash Table for storing and retrieving data using key-value pairs.

---

## 📌 Overview

A Hash Table is a data structure that provides efficient storage and lookup using a hash function.

Each key is converted into an index, allowing values to be accessed efficiently.

This implementation demonstrates the fundamental concepts behind hash tables, including hashing and collision handling.

---

## 🧩 Implementation

Main directory:

HashTable/

The module contains the Hash Table implementation and its supporting components.

---

## ⚙️ Core Operations

| Operation | Description |
|---|---|
| Insert | Add a key-value pair |
| Search | Find a value using a key |
| Update | Change the value associated with a key |
| Delete | Remove a key-value pair |
| Display | Show stored entries |
| Contains | Check whether a key exists |
| Clear | Remove all entries |

---

## 🔑 Key-Value Concept

Hash Tables store information using pairs:

key → value

Example:

name → Mohammed

age → 22

city → Taiz

The key is processed by a hash function to determine where the value should be stored.

---

## 💥 Collision Handling

A collision occurs when two different keys produce the same hash index.

A Hash Table must handle these collisions to continue storing data correctly.

Common collision-handling techniques include:

- Chaining
- Open Addressing
- Linear Probing
- Quadratic Probing

The implementation demonstrates collision handling according to the techniques provided in the module.

---

## 🧮 Hashing

A hash function converts a key into an integer index.

Conceptually:

hash(key) → index

A good hash function distributes keys across the available table positions to reduce collisions.

---

## ⏱️ Time Complexity

Average case:

| Operation | Complexity |
|---|---:|
| Insert | O(1) |
| Search | O(1) |
| Update | O(1) |
| Delete | O(1) |

Worst case:

| Operation | Complexity |
|---|---:|
| Insert | O(n) |
| Search | O(n) |
| Update | O(n) |
| Delete | O(n) |

Worst-case performance can occur when many keys collide.

---

## 💾 Space Complexity

The Hash Table requires:

O(n)

space for n stored elements.

---

## 🎯 Educational Purpose

This module demonstrates:

- Hash Tables
- Key-value storage
- Hash functions
- Hash indexes
- Collision handling
- Searching
- Insertion
- Deletion
- Updating values
- Average and worst-case complexity

---

## ▶️ Running

From the project root:

python app.py

The Hash Table can also be used directly through its implementation classes.

---

## 🔗 Part of the Project

This Hash Table implementation is part of the Data Structures Project, which also includes:

- Array
- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Binary Search Tree
- Graph
- Heap
- Sorting Algorithms
- Searching Algorithms
