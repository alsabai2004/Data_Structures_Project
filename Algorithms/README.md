# 🔎 Searching Algorithms

A Python implementation of common searching algorithms for locating elements in collections.

---

## 📌 Overview

Searching algorithms are used to determine whether a specific value exists in a collection and, when possible, identify its position.

This module focuses on fundamental searching techniques and their algorithmic complexity.

---

## 🧩 Implementation

Main directory:

Algorithms/

The searching implementations are organized inside the searching module.

---

## ⚙️ Searching Algorithms

| Algorithm | Description |
|---|---|
| Linear Search | Checks elements sequentially |
| Binary Search | Repeatedly divides a sorted collection |
| Graph Search | Traverses graph vertices using search techniques |

---

## 🔍 Linear Search

Linear Search examines elements one by one until the requested value is found or the collection ends.

Example:

Data:

10, 20, 30, 40, 50

Searching for 40:

10 → 20 → 30 → 40

Time Complexity:

O(n)

Space Complexity:

O(1)

---

## 🔎 Binary Search

Binary Search works on sorted data.

The algorithm compares the target with the middle element and eliminates half of the remaining search space after each comparison.

Example:

Data:

10, 20, 30, 40, 50, 60, 70

Searching for 60:

1. Check the middle.
2. Determine which half may contain the value.
3. Repeat until the value is found.

Time Complexity:

O(log n)

Space Complexity:

O(1) for an iterative implementation.

---

## 🌐 Graph Searching

Graph traversal algorithms can also be used to search through connected vertices.

The project Graph implementation includes:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both can traverse a graph in:

O(V + E)

where:

- V = number of vertices
- E = number of edges

---

## 📊 Complexity Comparison

| Algorithm | Best | Average | Worst |
|---|---:|---:|---:|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |
| BFS | O(1)* | O(V + E) | O(V + E) |
| DFS | O(1)* | O(V + E) | O(V + E) |

*Depends on where the target is located and the traversal structure.

---

## 🎯 Educational Purpose

This module demonstrates:

- Searching concepts
- Linear Search
- Binary Search
- Sorted-data requirements
- Graph traversal
- Algorithm complexity
- Iterative and recursive approaches

---

## 🔗 Part of the Project

This module is part of the Data Structures Project, which also includes:

- Array
- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Binary Search Tree
- Graph
- Heap
- Hash Table
- Sorting Algorithms
