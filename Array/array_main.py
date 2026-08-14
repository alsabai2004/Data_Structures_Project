from .array import Arrays


def array_oprea():
    while True:
        print("\n" + "=" * 40)
        print("                ARRAY")
        print("=" * 40)
        print("1. Create Array")
        print("2. Exit")
        print("=" * 40)

        choice_array = input("Enter your choice: ").strip()

        if choice_array == "1":
            try:
                size = int(input("Enter the size of your array: "))

                if size < 0:
                    print("Array size cannot be negative.")
                    continue

                array_play = Arrays(size)

            except ValueError:
                print("Please enter a valid integer.")
                continue

            while True:
                print("\n" + "-" * 40)
                print("             ARRAY OPERATIONS")
                print("-" * 40)
                print("1. Insert")
                print("2. Display all elements")
                print("3. Delete one item")
                print("4. Delete all occurrences")
                print("5. Keep first occurrence")
                print("6. Search")
                print("7. Get array length")
                print("8. Check if empty")
                print("9. Clear array")
                print("10. Back")
                print("-" * 40)

                choice_playarray = input("Enter your choice: ").strip()

                if choice_playarray == "1":
                    array_play.insert()

                elif choice_playarray == "2":
                    array_play.display()

                elif choice_playarray == "3":
                    try:
                        item = int(input("Enter the element: "))
                        array_play.deleteitem(item)
                    except ValueError:
                        print("Please enter a valid integer.")

                elif choice_playarray == "4":
                    try:
                        item = int(input("Enter the element: "))
                        array_play.deleteALLItem(item)
                    except ValueError:
                        print("Please enter a valid integer.")

                elif choice_playarray == "5":
                    try:
                        item = int(input("Enter the element: "))
                        array_play.notfirst(item)
                    except ValueError:
                        print("Please enter a valid integer.")

                elif choice_playarray == "6":
                    try:
                        item = int(input("Enter the element: "))

                        if array_play.search(item):
                            print(f"Value {item} exists in the array.")
                        else:
                            print(f"Value {item} was not found.")

                    except ValueError:
                        print("Please enter a valid integer.")

                elif choice_playarray == "7":
                    print("Array length:", array_play.get_length())

                elif choice_playarray == "8":
                    if array_play.is_empty():
                        print("Array is empty.")
                    else:
                        print("Array contains elements.")

                elif choice_playarray == "9":
                    array_play.clear()
                    print("Array cleared successfully.")

                elif choice_playarray == "10":
                    print("Returning to Array menu...")
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice_array == "2":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    array_oprea()
