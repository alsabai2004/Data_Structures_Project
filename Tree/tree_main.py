from .binary_tree import BinarySearchTree


def tree_oprea():
    tree = BinarySearchTree()

    while True:
        print("\n" + "=" * 50)
        print("             BINARY SEARCH TREE")
        print("=" * 50)
        print("1.  Insert")
        print("2.  Search")
        print("3.  Delete")
        print("4.  Inorder Traversal")
        print("5.  Preorder Traversal")
        print("6.  Postorder Traversal")
        print("7.  Level-order Traversal")
        print("8.  Find Minimum")
        print("9.  Find Maximum")
        print("10. Tree Height")
        print("11. Display Tree")
        print("12. Check if Empty")
        print("13. Get Size")
        print("14. Clear Tree")
        print("15. Back to Main Menu")
        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                value = int(input("Enter value to insert: "))

                if tree.insert(value):
                    print(f"Value {value} inserted successfully.")
                else:
                    print(f"Value {value} already exists.")

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            try:
                value = int(input("Enter value to search: "))

                if tree.search(value):
                    print(f"Value {value} exists in the tree.")
                else:
                    print(f"Value {value} was not found.")

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "3":
            try:
                value = int(input("Enter value to delete: "))

                if tree.delete(value):
                    print(f"Value {value} deleted successfully.")
                else:
                    print(f"Value {value} was not found.")

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "4":
            result = tree.inorder()
            print("Inorder:", result if result else "Tree is empty.")

        elif choice == "5":
            result = tree.preorder()
            print("Preorder:", result if result else "Tree is empty.")

        elif choice == "6":
            result = tree.postorder()
            print("Postorder:", result if result else "Tree is empty.")

        elif choice == "7":
            result = tree.levelorder()
            print("Level-order:", result if result else "Tree is empty.")

        elif choice == "8":
            minimum = tree.find_min()

            if minimum is None:
                print("Tree is empty.")
            else:
                print("Minimum value:", minimum)

        elif choice == "9":
            maximum = tree.find_max()

            if maximum is None:
                print("Tree is empty.")
            else:
                print("Maximum value:", maximum)

        elif choice == "10":
            height = tree.height()

            if height == -1:
                print("Tree is empty.")
            else:
                print("Tree height:", height)

        elif choice == "11":
            print("\nTree Structure:")
            tree.display()

        elif choice == "12":
            if tree.is_empty():
                print("Tree is empty.")
            else:
                print("Tree contains elements.")

        elif choice == "13":
            print("Number of nodes:", tree.get_size())

        elif choice == "14":
            tree.clear()
            print("Tree cleared successfully.")

        elif choice == "15":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tree_oprea()
