from .deque import Deque


def deque_oprea():
    dq = Deque()

    while True:
        print("\n" + "=" * 45)
        print("                 DEQUE")
        print("=" * 45)
        print("1. Add Front")
        print("2. Add Rear")
        print("3. Remove Front")
        print("4. Remove Rear")
        print("5. Front")
        print("6. Rear")
        print("7. Display")
        print("8. Size")
        print("9. Check Empty")
        print("10. Clear")
        print("11. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            dq.add_front(input("Enter value: "))

        elif choice == "2":
            dq.add_rear(input("Enter value: "))

        elif choice == "3":
            print("Removed:", dq.remove_front())

        elif choice == "4":
            print("Removed:", dq.remove_rear())

        elif choice == "5":
            print("Front:", dq.front())

        elif choice == "6":
            print("Rear:", dq.rear())

        elif choice == "7":
            dq.display()

        elif choice == "8":
            print("Size:", dq.size())

        elif choice == "9":
            print("Empty." if dq.is_empty() else "Not empty.")

        elif choice == "10":
            dq.clear()
            print("Deque cleared.")

        elif choice == "11":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    deque_oprea()
