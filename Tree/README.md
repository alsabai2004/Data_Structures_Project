# 🌳 Binary Search Tree

A Python implementation of a Binary Search Tree (BST) with insertion, searching, deletion, traversal, and tree-analysis operations.

---

## 📌 Overview

A Binary Search Tree is a hierarchical data structure where each node follows this ordering rule:

- Values smaller than the node are stored in the left subtree.
- Values greater than the node are stored in the right subtree.
- Duplicate values are ignored.

---

## 🧩 Implementation

Main files:

Tree/
- binary_tree.py
- tree_main.py

### binary_tree.py

Contains the Node and BinarySearchTree implementations.

### tree_main.py

Provides the interactive terminal menu for managing the tree.

---

## ⚙️ Supported Operations

| Operation | Description |
|---|---|
| insert() | Insert a value |
| search() | Search for a value |
| delete() | Delete a value |
| inorder() | Left → Root → Right traversal |
| preorder() | Root → Left → Right traversal |
| postorder() | Left → Right → Root traversal |
| find_min() | Find the minimum value |
| find_max() | Find the maximum value |
| height() | Calculate tree height |
| is_empty() | Check whether the tree is empty |
| display() | Display tree structure |

---

## 🧠 Example Tree

For the values:

50, 30, 70, 20, 40, 60, 80

The tree structure is:

50
├── 30
│   ├── 20
│   └── 40
└── 70
    ├── 60
    └── 80

---

## 🔄 Tree Traversals

### Inorder

Visits:

Left → Root → Right

For the example tree:

20, 30, 40, 50, 60, 70, 80

In a valid BST, inorder traversal produces values in sorted order.

### Preorder

Visits:

Root → Left → Right

### Postorder

Visits:

Left → Right → Root

---

## 🗑️ Deletion

The implementation handles the three main deletion cases:

1. Node with no children
2. Node with one child
3. Node with two children

For a node with two children, the implementation uses the minimum node from the right subtree as the replacement.

---

## ⏱️ Time Complexity

Average case:

| Operation | Complexity |
|---|---:|
| Insert | O(log n) |
| Search | O(log n) |
| Delete | O(log n) |
| Find Minimum | O(log n) |
| Find Maximum | O(log n) |

Worst case for an unbalanced tree:

| Operation | Complexity |
|---|---:|
| Insert | O(n) |
| Search | O(n) |
| Delete | O(n) |

Traversal operations require O(n).

---

## 💾 Space Complexity

The tree requires O(n) space for n nodes.

Recursive traversal and deletion operations may additionally use O(h) call-stack space, where h is the tree height.

---

## ▶️ Running the Module

From the project root:

python -m Tree.tree_main

Or run the complete project:

python app.py

Then select:

5. Binary Search Tree

---

## 🎯 Educational Purpose

This module demonstrates:

- Binary Search Tree concepts
- Hierarchical data structures
- Node insertion
- Searching
- Node deletion
- Tree traversal
- Minimum and maximum values
- Tree height
- Recursive algorithms
- Time and space complexity

---

## 🔗 Part of the Project

This Binary Search Tree is part of the Data Structures Project, which also includes:

- Array
- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Graph
- Heap
- Hash Table
- Sorting Algorithms
- Searching Algorithms
