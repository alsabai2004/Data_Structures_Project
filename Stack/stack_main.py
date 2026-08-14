from .stack_Array import Stack
from .stack_linkedlist import Stack_linkedlist


def Stack_oprea():
    while True:
        print("\n" + "=" * 45)
        print("                  STACK")
        print("=" * 45)
        print("1. Array Implementation")
        print("2. Linked List Implementation")
        print("3. Exit")
        print("=" * 45)

        choice_implement = input("Enter your choice: ").strip()

        if choice_implement == "1":
            _array_stack_menu()

        elif choice_implement == "2":
            _linked_stack_menu()

        elif choice_implement == "3":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


def _array_stack_menu():
    try:
        size = int(input("Enter the size of the stack: "))

        if size <= 0:
            print("Stack size must be greater than zero.")
            return

        stack = Stack(size)

    except ValueError:
        print("Please enter a valid integer.")
        return

    while True:
        print("\n" + "-" * 45)
        print("             ARRAY STACK")
        print("-" * 45)
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Search")
        print("6. Delete Element")
        print("7. Get Size")
        print("8. Check if Empty")
        print("9. Clear Stack")
        print("10. Back")
        print("-" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("Enter the value: ")
            stack.push(value)

        elif choice == "2":
            value = stack.pop()

            if value is not None:
                print("Popped:", value)

        elif choice == "3":
            value = stack.peek()

            if value is not None:
                print("Top:", value)

        elif choice == "4":
            stack.display()

        elif choice == "5":
            value = input("Enter the value to search: ")
            position = stack.search(value)

            if position == -1:
                print(f"Value {value} was not found.")
            else:
                print(f"Value {value} found at position {position}.")

        elif choice == "6":
            value = input("Enter the value to delete: ")
            stack.deleteElement(value)

        elif choice == "7":
            print("Stack size:", stack.get_size())

        elif choice == "8":
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack contains elements.")

        elif choice == "9":
            stack.clear()
            print("Stack cleared successfully.")

        elif choice == "10":
            break

        else:
            print("Invalid choice. Please try again.")


def _linked_stack_menu():
    stack = Stack_linkedlist()

    while True:
        print("\n" + "-" * 45)
        print("           LINKED LIST STACK")
        print("-" * 45)
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Search")
        print("6. Get Size")
        print("7. Check if Empty")
        print("8. Clear Stack")
        print("9. Make Copy")
        print("10. Back")
        print("-" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("Enter the value: ")
            stack.push(value)

        elif choice == "2":
            value = stack.pop()

            if value is not None:
                print("Popped:", value)

        elif choice == "3":
            value = stack.peek()

            if value is not None:
                print("Top:", value)

        elif choice == "4":
            stack.display()

        elif choice == "5":
            value = input("Enter the value to search: ")
            position = stack.search(value)

            if position == -1:
                print(f"Value {value} was not found.")
            else:
                print(f"Value {value} found at position {position}.")

        elif choice == "6":
            print("Stack size:", stack.get_size())

        elif choice == "7":
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack contains elements.")

        elif choice == "8":
            stack.clear()
            print("Stack cleared successfully.")

        elif choice == "9":
            copied_stack = stack.make_copy()
            print("Copied stack:")
            copied_stack.display()

        elif choice == "10":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Stack_oprea()
