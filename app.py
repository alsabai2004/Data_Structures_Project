from Array.array_main import array_oprea
from Queue.queue_main import Queue_oprea
from Stack.stack_main import Stack_oprea
from Tree.tree_main import tree_oprea
from Graph.graph_main import graph_oprea
from Heap.heap_main import heap_oprea
from HashTable.hash_main import hash_oprea
from Deque.deque_main import deque_oprea
from Recursion.recursion_main import recursion_oprea
from Sorting.sorting_main import sorting_oprea

import importlib.util
from pathlib import Path


def load_linked_list():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "linkedlist" / "Single LinkedLists" / "linked_main.py"

    spec = importlib.util.spec_from_file_location(
        "linked_main",
        file_path
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module.Linked_oprea


Linked_oprea = load_linked_list()


def main():
    while True:
        print("\n" + "=" * 50)
        print("          DATA STRUCTURES PROJECT")
        print("=" * 50)
        print("1. Array")
        print("2. Linked List")
        print("3. Stack")
        print("4. Queue")
        print("5. Binary Search Tree")
        print("6. Graph")
        print("7. Heap & Priority Queue")
        print("8. Hash Table")
        print("9. Deque")
        print("10. Recursion")
        print("11. Sorting Algorithms")
        print("12. Exit")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            array_oprea()

        elif choice == "2":
            Linked_oprea()

        elif choice == "3":
            Stack_oprea()

        elif choice == "4":
            Queue_oprea()

        elif choice == "5":
            tree_oprea()

        elif choice == "6":
            graph_oprea()

        elif choice == "7":
            heap_oprea()

        elif choice == "8":
            hash_oprea()

        elif choice == "9":
            deque_oprea()

        elif choice == "10":
            recursion_oprea()

        elif choice == "11":
            sorting_oprea()

        elif choice == "12":
            print("Exiting Data Structures Project...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
