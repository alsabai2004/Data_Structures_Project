from .hash_table import HashTable


def hash_oprea():
    try:
        capacity = int(input("Enter hash table capacity: "))
        table = HashTable(capacity)
    except ValueError:
        print("Invalid capacity.")
        return

    while True:
        print("\n" + "=" * 45)
        print("              HASH TABLE")
        print("=" * 45)
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Size")
        print("6. Check Empty")
        print("7. Clear")
        print("8. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            if table.insert(key, value):
                print("Key inserted successfully.")
            else:
                print("Key already exists. Value updated.")

        elif choice == "2":
            key = input("Enter key: ")
            value = table.search(key)
            if value is None:
                print("Key was not found.")
            else:
                print("Value:", value)

        elif choice == "3":
            key = input("Enter key: ")
            if table.delete(key):
                print("Key deleted successfully.")
            else:
                print("Key was not found.")

        elif choice == "4":
            table.display()

        elif choice == "5":
            print("Size:", table.size())

        elif choice == "6":
            print("Empty." if table.is_empty() else "Not empty.")

        elif choice == "7":
            table.clear()
            print("Hash Table cleared.")

        elif choice == "8":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    hash_oprea()
