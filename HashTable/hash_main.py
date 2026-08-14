from .hash_table import HashTable


def hash_oprea():
    table = HashTable()

    while True:
        print("\n" + "=" * 45)
        print("              HASH TABLE")
        print("=" * 45)
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Keys")
        print("6. Values")
        print("7. Items")
        print("8. Size")
        print("9. Check Empty")
        print("10. Clear")
        print("11. Back")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            if table.insert(key, value):
                print("Key inserted successfully.")
            else:
                print("Key updated successfully.")

        elif choice == "2":
            key = input("Enter key: ")
            value = table.search(key)
            print("Value:", value if value is not None else "Key not found.")

        elif choice == "3":
            key = input("Enter key: ")
            print("Deleted successfully." if table.delete(key) else "Key not found.")

        elif choice == "4":
            table.display()

        elif choice == "5":
            print("Keys:", table.keys())

        elif choice == "6":
            print("Values:", table.values())

        elif choice == "7":
            print("Items:", table.items())

        elif choice == "8":
            print("Size:", table.get_size())

        elif choice == "9":
            print("Hash table is empty." if table.is_empty() else "Hash table contains elements.")

        elif choice == "10":
            table.clear()
            print("Hash table cleared successfully.")

        elif choice == "11":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    hash_oprea()
