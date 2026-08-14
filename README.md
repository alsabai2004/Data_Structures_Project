# 🧠 Data Structures and Algorithms Learning Project

A comprehensive Python project for learning and practicing fundamental Data Structures and Algorithms through interactive terminal-based implementations.

The project is designed for learning, practicing, and understanding how common data structures work internally, including their operations, traversal methods, searching techniques, and algorithmic complexity.


---

## 📌 Project Overview

This project provides practical implementations of several important data structures and algorithms using Python.

The main goal is to demonstrate how data structures operate through clean, modular, and interactive implementations.

The project includes:

### 📦 Array

### 🔗 Singly Linked List

### 🔗 Doubly Linked List

### 📚 Stack

### 🚶 Queue

### 🌳 Binary Search Tree

### 🕸️ Graph

### 🏔️ Min Heap

### #️⃣ Hash Table

### 🔄 Sorting Algorithms

### 🔎 Searching Algorithms



---

## 🗂️ Project Structure
```
data_structures_project/  
│  
├── Array/  
│   ├── array.py  
│   ├── array_main.py  
│   └── README.md  
│  
├── Stack/  
│   ├── stack_Array.py  
│   ├── stack_linkedlist.py  
│   ├── stack_main.py  
│   └── README.md  
│  
├── Queue/  
│   ├── queue_Array.py  
│   ├── queue_linkdlist.py  
│   ├── queue_main.py  
│   └── README.md  
│  
├── linkedlist/  
│   ├── Single LinkedLists/  
│   │   ├── linked.py  
│   │   ├── linked_main.py  
│   │   └── README.md  
│   │  
│   └── Double LinkedList/  
│       ├── DLinkedList.py  
│       ├── README.md  
│       └── ...  
│  
├── Tree/  
│   ├── binary_tree.py  
│   ├── tree_main.py  
│   └── README.md  
│  
├── Graph/  
│   ├── graph.py  
│   ├── graph_main.py  
│   └── README.md  
│  
├── Heap/  
│   ├── min_heap.py  
│   └── README.md  
│  
├── HashTable/  
│   ├── ...  
│   └── README.md  
│  
├── Algorithms/  
│   ├── searching/  
│   ├── ...  
│   └── README.md  
│  
├── Sorting/  
│   ├── ...  
│   └── README.md  
│  
├── models/  
│   ├── node.py  
│   └── dnode.py  
│  
└── app.py

```
---

## 🧩 Data Structures

📦 Array

The Array implementation provides operations for storing, accessing, searching, inserting, and deleting elements.

Supported operations include:

Insert

Search

Delete one item

Delete all occurrences

Remove duplicates

Get element

Get length

Check empty

Clear

Display


---

## 🔗 Singly Linked List

The Singly Linked List stores elements using nodes connected through a Next reference.

Supported operations include:

Append

Add after

Add at index

Delete by value

Delete by index

Delete first

Delete last

Find

Find at position

Delete until value

Clear

Display


---

## 🔗 Doubly Linked List

The Doubly Linked List extends the linked-list concept by maintaining connections in both directions.

Each node contains:

Data

Previous reference

Next reference

Supported operations include:

Add first

Add last

Add at index

Add before

Add after

Delete first

Delete last

Delete item

Delete at index

Delete before

Delete after

Forward traversal

Reverse traversal

Clear


---

## 📚 Stack

The project provides Stack implementations using:

Array

Linked List

A Stack follows the:

LIFO — Last In, First Out

principle.

Supported operations include:

Push

Pop

Peek

Check empty

Display


---

## 🚶 Queue

The project provides Queue implementations using:

Array

Linked List

A Queue follows the:

FIFO — First In, First Out

principle.

Supported operations include:

Enqueue

Dequeue

Get front

Get rear

Check empty

Display


---

## 🌳 Binary Search Tree

The Binary Search Tree organizes values according to the BST property:
```
Left Subtree < Root < Right Subtree
```
Supported operations include:

Insert

Search

Delete

Find minimum

Find maximum

Tree height

Inorder traversal

Preorder traversal

Postorder traversal

Check empty

Display tree

Example:  
  ```
          50  
        /    \  
      30      70  
     /  \    /  \  
   20   40  60   80
```

---

## 🕸️ Graph

The Graph implementation uses an adjacency-list representation.

It supports:

Directed graphs

Undirected graphs

Supported operations include:

Add vertex

Remove vertex

Add edge

Remove edge

Check vertex

Check edge

Get neighbors

BFS

DFS

Vertex count

Edge count

Clear graph

Display graph


---

## 🏔️ Min Heap

The project includes a Min Heap implementation.

In a Min Heap, the smallest element is always located at the root.

Supported concepts include:

Insert

Extract minimum

Peek

Heapify up

Heapify down

Size

Empty check

| Operation | Time Complexity |  
|---|---:|  
| Insert | O(log n) |  
| Extract Min | O(log n) |  
| Peek | O(1) |


---

## #️⃣ Hash Table

The Hash Table provides key-value storage using hashing.

The implementation demonstrates:

Key-value storage

Hashing

Index calculation

Collision handling

Insert

Search

Update

Delete

Clear

Display

Average-case lookup, insertion, and deletion are typically:
```
O(1)
```

---

## 🔎 Searching Algorithms

The project includes fundamental searching techniques such as:

Linear Search

Binary Search

Graph Searching

Linear Search

Sequentially checks elements until the requested value is found.
```
Time: O(n)
```
Binary Search

Works on sorted data and repeatedly divides the search range into two halves.
```
Time: O(log n)
```
Graph Search

Graph traversal is supported through:

Breadth-First Search

Depth-First Search
```
BFS: O(V + E)
DFS: O(V + E)
```

---

## 🔄 Sorting Algorithms

The project includes common sorting concepts and implementations such as:

Bubble Sort

Selection Sort

Insertion Sort

Merge Sort

Quick Sort

Heap Sort

Complexity ranges from simple O(n²) algorithms to efficient divide-and-conquer algorithms such as Merge Sort and average-case Quick Sort.


---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Python 3 | Runtime environment |
| Object-Oriented Programming | Project architecture |
| Classes & Objects | Data structure modeling |
| Recursion | Tree and algorithm operations |
| Lists | Internal data storage |
| Dictionaries | Graph and Hash Table structures |
| Sets | Visited-node tracking |
| `collections.deque` | Efficient BFS queue |
| Terminal / Console | Interactive user interface |
| Git | Version control |
| GitHub | Project hosting |



---

## 🧠 Concepts Demonstrated

This project demonstrates practical knowledge of:

Linear Data Structures

Non-Linear Data Structures

Nodes

Pointers / References

Arrays

Linked Lists

Stacks

Queues

Trees

Graphs

Heaps

Hash Tables

Searching

Sorting

Recursion

Traversal

Hashing

Collision Handling

Algorithm Complexity

Time Complexity

Space Complexity

Modular Python Programming


---

## ⏱️ Complexity Overview

| Data Structure / Algorithm | Typical Complexity |
|---|---:|
| Array Access | O(1) |
| Array Search | O(n) |
| Linked List Search | O(n) |
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Queue Enqueue | O(1) |
| Queue Dequeue | O(1) |
| BST Search | O(log n) average |
| BST Insert | O(log n) average |
| BST Delete | O(log n) average |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Heap Insert | O(log n) |
| Heap Extract Min | O(log n) |
| Heap Peek | O(1) |
| Hash Table Search | O(1) average |
| Linear Search | O(n) |
| Binary Search | O(log n) |
| Merge Sort | O(n log n) |
| Quick Sort | O(n log n) average |
| Bubble Sort | O(n²) |
| Selection Sort | O(n²) |
| Insertion Sort | O(n²) average |


> Actual complexity may vary depending on implementation details and input structure.




---

## 🖥️ Running the Project

Clone the repository:
```
git clone https://github.com/alsabai2004/Data_Structures_Project.git
```
Enter the project directory:
```
cd Data_Structures_Project
```
Run the main application:
```
python app.py
```
The application provides an interactive terminal interface for accessing the different data structures.


---

## 🧪 Validation

The project has been tested using:
```
python -m compileall -q .
```
Import validation:
```
python -c "import app; print('ALL IMPORTS OK')"
```
The project modules were also tested individually through functional tests covering:

Array operations

Array Stack

Linked Stack

Array Queue

Linked Queue

Binary Search Tree

Graph

Singly Linked List

Doubly Linked List

Example successful validation:
```
============================================================
        DATA STRUCTURES - FULL TEST
============================================================
[OK] Array
[OK] Array Stack
[OK] Linked Stack
[OK] Array Queue
[OK] Linked Queue
[OK] Binary Search Tree
[OK] Graph
============================================================
ALL FULL TESTS PASSED SUCCESSFULLY
============================================================
```
---

## 📚 Documentation

Each major component contains its own README with details about:

Purpose

Implementation

Supported operations

Examples

Time complexity

Space complexity

Educational concepts

Available documentation includes:
```
Array/README.md
Queue/README.md
Tree/README.md
Graph/README.md
Heap/README.md
HashTable/README.md
Sorting/README.md
Algorithms/README.md
```

---

## 🎯 Project Goals

The main goals of this project are:

1. Understand fundamental data structures.


2. Implement structures manually using Python.


3. Practice Object-Oriented Programming.


4. Understand how common operations work internally.


5. Practice searching and sorting algorithms.


6. Analyze time and space complexity.


7. Build modular and reusable Python code.


8. Provide interactive terminal-based demonstrations.




---

## 🚀 Future Improvements

Possible future enhancements include:

More sorting algorithms

More searching algorithms

Priority Queue

AVL Tree

Red-Black Tree

Weighted Graph

Dijkstra's Algorithm

A* Search

Graph shortest-path algorithms

Improved exception handling

Automated unit tests

Performance benchmarking

Visualization of data structures

More detailed CLI interfaces

Type hints

Python documentation standards


---

# 👨‍💻 Author

## Eng\ Mohammed Najeeb Abd-Ulrazzaq Al-Sabai 

## Computer Networks & Cyber Security Student

---

## 📜 License

This project is intended primarily for educational and learning purposes.

You may study, modify, and extend the implementation for educational and personal projects.


---

## ⭐ Support

If you find this project useful for learning Data Structures and Algorithms, consider giving the repository a ⭐ on GitHub.


---

## 🔗 Repository

https://github.com/alsabai2004/Data_Structures_Project


---

## 🏁 Conclusion

This project brings together fundamental Data Structures and Algorithms in one modular Python application.

It provides practical implementations of linear and non-linear data structures, searching and sorting algorithms, traversal techniques, and complexity analysis.

The project is designed to grow over time as more advanced algorithms and data structures are added.
