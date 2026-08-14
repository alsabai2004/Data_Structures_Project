from .sorting import Sorting


def sorting_oprea():
    while True:
        print("\n" + "=" * 45)
        print("           SORTING ALGORITHMS")
        print("=" * 45)
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Check if Sorted")
        print("7. Back")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "7":
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice.")
            continue

        try:
            data = list(map(int, input("Enter numbers separated by spaces: ").split()))
        except ValueError:
            print("Please enter valid integers.")
            continue

        if choice == "1":
            print("Result:", Sorting.bubble_sort(data))
        elif choice == "2":
            print("Result:", Sorting.selection_sort(data))
        elif choice == "3":
            print("Result:", Sorting.insertion_sort(data))
        elif choice == "4":
            print("Result:", Sorting.merge_sort(data))
        elif choice == "5":
            print("Result:", Sorting.quick_sort(data))
        elif choice == "6":
            print("Sorted." if Sorting.is_sorted(data) else "Not sorted.")


if __name__ == "__main__":
    sorting_oprea()
