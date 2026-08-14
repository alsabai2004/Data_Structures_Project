# 🕸️ Graph Data Structure

A Python implementation of a Graph data structure using an adjacency-list representation.

---

## 📌 Overview

A Graph is a non-linear data structure consisting of vertices and edges.

This implementation supports both:

- Undirected Graphs
- Directed Graphs

The graph is internally represented using a Python dictionary where each vertex stores its list of neighboring vertices.

---

## 🧩 Implementation

Main files:

Graph/
- graph.py
- graph_main.py

### graph.py

Contains the Graph class and its core operations.

### graph_main.py

Provides the interactive terminal menu for creating and manipulating graphs.

---

## ⚙️ Supported Operations

| Operation | Description |
|---|---|
| add_vertex() | Add a new vertex |
| remove_vertex() | Remove a vertex and connected edges |
| add_edge() | Add an edge |
| remove_edge() | Remove an edge |
| has_vertex() | Check whether a vertex exists |
| has_edge() | Check whether an edge exists |
| get_vertices() | Return all vertices |
| get_neighbors() | Return neighboring vertices |
| bfs() | Breadth-First Search |
| dfs() | Depth-First Search |
| display() | Display adjacency list |
| clear() | Remove the entire graph |
| is_empty() | Check whether graph is empty |
| vertex_count() | Return number of vertices |
| edge_count() | Return number of edges |

---

## 🔀 Graph Types

### Undirected Graph

Edges work in both directions.

Example:

A — B

If an edge exists between A and B:

A can reach B, and B can reach A.

### Directed Graph

Edges have a specific direction.

Example:

A → B

A can reach B, but B does not automatically reach A.

---

## 🔎 Breadth-First Search

BFS explores the graph level by level.

It uses a queue to keep track of vertices that need to be visited.

Example graph:

A → B → D
A → C → D

BFS starting from A:

A → B → C → D

---

## 🔍 Depth-First Search

DFS explores as deeply as possible before backtracking.

It is implemented using recursion.

For the example graph, DFS starting from A can produce:

A → B → D → C

The exact traversal order depends on the order in which neighbors were added.

---

## 📋 Adjacency List

The graph uses an adjacency-list representation.

Example:

A → B, C
B → A, D
C → A, D
D → B, C

This representation is efficient for graphs where the number of edges is relatively small compared with the number of possible edges.

---

## ⏱️ Time Complexity

Let V represent the number of vertices and E represent the number of edges.

| Operation | Complexity |
|---|---:|
| Add Vertex | O(1) |
| Remove Vertex | O(V + E) |
| Add Edge | O(1) average |
| Remove Edge | O(V) in the worst case |
| Search Vertex | O(1) average |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Get Neighbors | O(1) |
| Vertex Count | O(1) |
| Edge Count | O(V) |

---

## 💾 Space Complexity

The adjacency-list representation requires:

O(V + E)

space.

BFS additionally uses a queue and visited set.

DFS additionally uses a visited set and recursion stack.

---

## ▶️ Running the Module

From the project root:

python -m Graph.graph_main

Or run the complete project:

python app.py

Then select:

6. Graph

---

## 🎯 Educational Purpose

This module demonstrates:

- Graph concepts
- Vertices and edges
- Directed graphs
- Undirected graphs
- Adjacency lists
- Breadth-First Search
- Depth-First Search
- Graph traversal
- Graph statistics
- Time and space complexity

---

## 🔗 Part of the Project

This Graph implementation is part of the Data Structures Project, which also includes:

- Array
- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Binary Search Tree
- Heap
- Hash Table
- Sorting Algorithms
- Searching Algorithms
