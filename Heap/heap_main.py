from .min_heap import MinHeap
from .max_heap import MaxHeap
from .priority_queue import PriorityQueue


def heap_oprea():
    while True:
        print("\n" + "=" * 45)
        print("                  HEAP")
        print("=" * 45)
        print("1. Min Heap")
        print("2. Max Heap")
        print("3. Priority Queue")
        print("4. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            _min_heap_menu()

        elif choice == "2":
            _max_heap_menu()

        elif choice == "3":
            _priority_queue_menu()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def _min_heap_menu():
    heap = MinHeap()

    while True:
        print("\nMIN HEAP")
        print("1. Insert")
        print("2. Extract Min")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Clear")
        print("7. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                heap.insert(int(input("Enter value: ")))
            except ValueError:
                print("Please enter an integer.")

        elif choice == "2":
            value = heap.extract_min()
            print("Extracted:", value)

        elif choice == "3":
            print("Minimum:", heap.peek())

        elif choice == "4":
            heap.display()

        elif choice == "5":
            print("Size:", heap.size())

        elif choice == "6":
            heap.clear()
            print("Heap cleared.")

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


def _max_heap_menu():
    heap = MaxHeap()

    while True:
        print("\nMAX HEAP")
        print("1. Insert")
        print("2. Extract Max")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Clear")
        print("7. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                heap.insert(int(input("Enter value: ")))
            except ValueError:
                print("Please enter an integer.")

        elif choice == "2":
            print("Extracted:", heap.extract_max())

        elif choice == "3":
            print("Maximum:", heap.peek())

        elif choice == "4":
            heap.display()

        elif choice == "5":
            print("Size:", heap.size())

        elif choice == "6":
            heap.clear()
            print("Heap cleared.")

        elif choice == "7":
            break

        else:
            print("Invalid choice.")


def _priority_queue_menu():
    queue = PriorityQueue()

    while True:
        print("\nPRIORITY QUEUE")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Clear")
        print("7. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("Enter value: ")

            try:
                priority = int(input("Enter priority (lower = higher priority): "))
                queue.enqueue(value, priority)
            except ValueError:
                print("Priority must be an integer.")

        elif choice == "2":
            print("Dequeued:", queue.dequeue())

        elif choice == "3":
            print("Next:", queue.peek())

        elif choice == "4":
            queue.display()

        elif choice == "5":
            print("Size:", queue.size())

        elif choice == "6":
            queue.clear()
            print("Priority Queue cleared.")

        elif choice == "7":
            break

        else:
            print("Invalid choice.")
