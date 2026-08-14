from .sorting import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)


def sorting_oprea():
    algorithms = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Selection Sort", selection_sort),
        "3": ("Insertion Sort", insertion_sort),
        "4": ("Merge Sort", merge_sort),
        "5": ("Quick Sort", quick_sort),
    }

    while True:
        print("\n" + "=" * 45)
        print("             SORTING ALGORITHMS")
        print("=" * 45)
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "6":
            break

        if choice not in algorithms:
            print("Invalid choice.")
            continue

        name, algorithm = algorithms[choice]

        try:
            data = list(map(
                int,
                input("Enter numbers separated by spaces: ").split()
            ))

            result = algorithm(data)

            print(f"{name} Result:")
            print(result)

        except ValueError:
            print("Please enter valid integers.")


if __name__ == "__main__":
    sorting_oprea()
