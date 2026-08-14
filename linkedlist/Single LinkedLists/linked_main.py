import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
SINGLE_DIR = Path(__file__).resolve().parent
DOUBLE_DIR = BASE_DIR / "linkedlist" / "Double LinkedList"

for directory in (BASE_DIR, SINGLE_DIR, DOUBLE_DIR):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))


from linked import Linkedlist
from DLinkedList import DLinkedList


def Linked_oprea():
    while True:
        print("\n" + "=" * 45)
        print("             LINKED LIST")
        print("=" * 45)
        print("1. Singly Linked List")
        print("2. Doubly Linked List")
        print("3. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            _single_linked_list_menu()

        elif choice == "2":
            _double_linked_list_menu()

        elif choice == "3":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


def _single_linked_list_menu():
    linked = Linkedlist()

    while True:
        print("\n" + "-" * 45)
        print("          SINGLY LINKED LIST")
        print("-" * 45)
        print("1. Add element")
        print("2. Add after value")
        print("3. Add at index")
        print("4. Delete by value")
        print("5. Delete by index")
        print("6. Get length")
        print("7. Find element")
        print("8. Find element at position")
        print("9. Display")
        print("10. Delete first")
        print("11. Delete last")
        print("12. Delete until value")
        print("13. Clear")
        print("14. Check empty")
        print("15. Back")
        print("-" * 45)

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                linked.append(input("Enter your data: "))

            elif choice == "2":
                item = input("Enter the element to add: ")
                after = input("Enter the value to add after: ")
                linked.addafter(item, after)

            elif choice == "3":
                item = input("Enter the element: ")
                index = int(input("Enter the index: "))
                linked.addat(item, index)

            elif choice == "4":
                item = input("Enter the data to delete: ")
                linked.delete_Data(item)

            elif choice == "5":
                index = int(input("Enter the index: "))
                linked.delete_index(index)

            elif choice == "6":
                print("Length:", linked.get_length())

            elif choice == "7":
                item = input("Enter the element to find: ")
                result = linked.find(item)

                if result is None:
                    print("Element not found.")
                else:
                    print("Element found:", result.data)

            elif choice == "8":
                position = int(input("Enter the position: "))
                result = linked.findAt(position)

                if result is not None:
                    print("Element:", result.data)

            elif choice == "9":
                linked.display()

            elif choice == "10":
                linked.deletefirst()

            elif choice == "11":
                linked.deletelast()

            elif choice == "12":
                item = input("Delete nodes until value: ")
                linked.deleteuntil(item)

            elif choice == "13":
                linked.clear()
                print("List cleared successfully.")

            elif choice == "14":
                if linked.is_empty():
                    print("Empty.")
                else:
                    print("Not empty.")

            elif choice == "15":
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid value.")


def _double_linked_list_menu():
    linked = DLinkedList()

    while True:
        print("\n" + "-" * 45)
        print("          DOUBLY LINKED LIST")
        print("-" * 45)
        print("1. Add first")
        print("2. Add last")
        print("3. Delete first")
        print("4. Delete last")
        print("5. Delete item")
        print("6. Delete at index")
        print("7. Add at index")
        print("8. Add after")
        print("9. Add before")
        print("10. Delete after")
        print("11. Delete before")
        print("12. Display")
        print("13. Display reverse")
        print("14. Clear")
        print("15. Back")
        print("-" * 45)

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                linked.addFirst(input("Enter data: "))

            elif choice == "2":
                linked.addLast(input("Enter data: "))

            elif choice == "3":
                linked.deleteFirst()

            elif choice == "4":
                linked.deleteLast()

            elif choice == "5":
                linked.deleteItem(input("Enter value: "))

            elif choice == "6":
                index = int(input("Enter index: "))
                linked.deleteAt(index)

            elif choice == "7":
                data = input("Enter data: ")
                index = int(input("Enter index: "))
                linked.addAt(data, index)

            elif choice == "8":
                data = input("Enter data: ")
                after = input("Add after value: ")
                linked.addAfter(data, after)

            elif choice == "9":
                data = input("Enter data: ")
                before = input("Add before value: ")
                linked.addBefore(data, before)

            elif choice == "10":
                item = input("Delete node after value: ")
                linked.deleteAfter(item)

            elif choice == "11":
                item = input("Delete node before value: ")
                linked.deleteBefore(item)

            elif choice == "12":
                linked.display()

            elif choice == "13":
                values = linked.reverse_to_list()

                if not values:
                    print("The list is empty.")
                else:
                    for value in values:
                        print(value)

            elif choice == "14":
                linked.clear()
                print("List cleared successfully.")

            elif choice == "15":
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid value.")


if __name__ == "__main__":
    Linked_oprea()
