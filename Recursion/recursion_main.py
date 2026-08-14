from .recursion import factorial, fibonacci, sum_numbers, binary_search


def recursion_oprea():
    while True:
        print("\n" + "=" * 45)
        print("                RECURSION")
        print("=" * 45)
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum 1..N")
        print("4. Recursive Binary Search")
        print("5. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                n = int(input("Enter N: "))
                print("Result:", factorial(n))

            elif choice == "2":
                n = int(input("Enter N: "))
                print("Result:", fibonacci(n))

            elif choice == "3":
                n = int(input("Enter N: "))
                print("Result:", sum_numbers(n))

            elif choice == "4":
                data = list(map(
                    int,
                    input("Enter sorted numbers separated by spaces: ").split()
                ))
                target = int(input("Enter target: "))
                print("Index:", binary_search(data, target))

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

        except ValueError as error:
            print("Invalid input:", error)


if __name__ == "__main__":
    recursion_oprea()
