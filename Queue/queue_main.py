from .queue_Array import Queue
from .queue_linkdlist import QueueLinked


def Queue_oprea():
    while True:
        print("\n" + "=" * 45)
        print("                 QUEUE")
        print("=" * 45)
        print("1. Array Implementation")
        print("2. Linked List Implementation")
        print("3. Exit")
        print("=" * 45)

        choice_implement = input("Enter your choice: ").strip()

        if choice_implement == "1":
            _array_queue_menu()

        elif choice_implement == "2":
            _linked_queue_menu()

        elif choice_implement == "3":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


def _array_queue_menu():
    try:
        size = int(input("Enter the size of the queue: "))

        if size <= 0:
            print("Queue size must be greater than zero.")
            return

        queue = Queue(size)

    except ValueError:
        print("Please enter a valid integer.")
        return

    while True:
        print("\n" + "-" * 45)
        print("             ARRAY QUEUE")
        print("-" * 45)
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Show Front")
        print("5. Show Rear")
        print("6. Delete Specific Item")
        print("7. Get Size")
        print("8. Check if Empty")
        print("9. Reset Queue")
        print("10. Back")
        print("-" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("Enter the value: ")
            queue.enqueue(value)

        elif choice == "2":
            result = queue.dequeue()

            if result is not None:
                print("Dequeued:", result)

        elif choice == "3":
            queue.display()

        elif choice == "4":
            result = queue.get_front()

            if result is not None:
                print("Front:", result)

        elif choice == "5":
            result = queue.get_rear()

            if result is not None:
                print("Rear:", result)

        elif choice == "6":
            value = input("Enter the item to delete: ")
            queue.deleteitem(value)

        elif choice == "7":
            print("Queue size:", queue.get_size())

        elif choice == "8":
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue contains elements.")

        elif choice == "9":
            queue.reset()
            print("Queue reset successfully.")

        elif choice == "10":
            break

        else:
            print("Invalid choice. Please try again.")


def _linked_queue_menu():
    queue = QueueLinked()

    while True:
        print("\n" + "-" * 45)
        print("           LINKED LIST QUEUE")
        print("-" * 45)
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Show Front")
        print("5. Show Rear")
        print("6. Get Size")
        print("7. Check if Empty")
        print("8. Clear Queue")
        print("9. Back")
        print("-" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("Enter the value: ")
            queue.enqueue(value)

        elif choice == "2":
            result = queue.dequeue()

            if result is not None:
                print("Dequeued:", result)

        elif choice == "3":
            queue.display()

        elif choice == "4":
            result = queue.getFront()

            if result is not None:
                print("Front:", result)

        elif choice == "5":
            result = queue.getRear()

            if result is not None:
                print("Rear:", result)

        elif choice == "6":
            print("Queue size:", queue.get_size())

        elif choice == "7":
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue contains elements.")

        elif choice == "8":
            queue.clear()
            print("Queue cleared successfully.")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Queue_oprea()
