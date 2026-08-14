from .searching import Searching


def algorithms_oprea():
    while True:
        print("\n" + "=" * 45)
        print("             ALGORITHMS")
        print("=" * 45)
        print("1. Binary Search")
        print("2. Back")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                data = list(map(int, input(
                    "Enter SORTED numbers separated by spaces: "
                ).split()))
                target = int(input("Enter target: "))

                result = Searching.binary_search(data, target)

                if result == -1:
                    print("Target not found.")
                else:
                    print(f"Target found at index {result}.")

            except ValueError:
                print("Please enter valid integers.")

        elif choice == "2":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    algorithms_oprea()
