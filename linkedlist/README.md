# 🔗 Linked List Data Structures

A Python implementation of Linked List data structures, including Singly Linked List and Doubly Linked List.

---

## 📌 Overview

Linked Lists are linear data structures where elements are stored in nodes.

Each node contains data and references that connect it to other nodes.

This module provides two implementations:

- Singly Linked List
- Doubly Linked List

---

## 🧩 Project Structure

linkedlist/
- Single LinkedLists/
  - linked.py
  - linked_main.py
- Double LinkedList/
  - DLinkedList.py

---

# ➡️ Singly Linked List

The Singly Linked List uses nodes where each node contains:

- Data
- Reference to the next node

Supported operations include:

- Append
- Add after a value
- Add at an index
- Delete by value
- Delete by index
- Delete first
- Delete last
- Delete until a value
- Find an element
- Find an element by position
- Get size
- Clear
- Display
- Check whether the list is empty
- Convert to Python list

---

## ⚙️ Singly Linked List Operations

| Operation | Description |
|---|---|
| append() | Add an element to the end |
| addafter() | Add an element after a value |
| addat() | Add an element at a position |
| delete_Data() | Delete an element by value |
| delete_index() | Delete an element by index |
| deletefirst() | Delete the first element |
| deletelast() | Delete the last element |
| find() | Search for a value |
| findAt() | Find an element by position |
| deleteuntil() | Delete elements until a value |
| get_size() | Return list size |
| clear() | Remove all elements |
| to_list() | Convert list to Python list |

---

# ↔️ Doubly Linked List

The Doubly Linked List uses nodes containing:

- Data
- Previous reference
- Next reference

It maintains both Head and Tail references.

Supported operations include:

- Add first
- Add last
- Add at index
- Add after
- Add before
- Delete first
- Delete last
- Delete item
- Delete at index
- Delete after
- Delete before
- Find
- Display
- Reverse display
- Get size
- Clear
- Convert to list
- Reverse to list

---

## ⚙️ Doubly Linked List Operations

| Operation | Description |
|---|---|
| addFirst() | Add an element at the beginning |
| addLast() | Add an element at the end |
| addAt() | Add an element at an index |
| addAfter() | Add an element after a value |
| addBefore() | Add an element before a value |
| deleteFirst() | Delete the first element |
| deleteLast() | Delete the last element |
| deleteItem() | Delete an element by value |
| deleteAt() | Delete an element by index |
| deleteAfter() | Delete the node after a value |
| deleteBefore() | Delete the node before a value |
| find() | Search for a value |
| display() | Display the list |
| reverse_to_list() | Return elements in reverse order |
| get_size() | Return list size |
| clear() | Clear the list |
| to_list() | Convert list to Python list |

---

## 🧠 Singly vs Doubly Linked List

| Feature | Singly Linked List | Doubly Linked List |
|---|---|---|
| Next reference | Yes | Yes |
| Previous reference | No | Yes |
| Forward traversal | Yes | Yes |
| Backward traversal | No | Yes |
| Memory usage | Lower | Higher |
| Implementation | Simpler | More complex |

---

## ⏱️ Time Complexity

| Operation | Singly | Doubly |
|---|---:|---:|
| Add First | O(1) | O(1) |
| Add Last | O(n) | O(1) |
| Search | O(n) | O(n) |
| Delete First | O(1) | O(1) |
| Delete Last | O(n) | O(1) |
| Insert at Position | O(n) | O(n) |
| Delete at Position | O(n) | O(n) |

---

## 💾 Space Complexity

For n nodes:

Singly Linked List:
O(n)

Doubly Linked List:
O(n)

The Doubly Linked List requires additional memory for previous-node references.

---

## ▶️ Running the Module

From the project root:

python 'linkedlist/Single LinkedLists/linked_main.py'

Or run the complete project:

python app.py

Then select:

2. Linked List

---

## 🎯 Educational Purpose

This module demonstrates:

- Node-based data structures
- Dynamic memory organization
- Linked node traversal
- Insertion and deletion
- Searching
- Singly linked structures
- Doubly linked structures
- Forward and backward traversal
- Time and space complexity

---

## 🔗 Part of the Project

The Linked List module is part of the Data Structures Project, which also includes:

- Array
- Stack
- Queue
- Binary Search Tree
- Graph
- Heap
- Hash Table
- Sorting Algorithms
- Searching Algorithms
