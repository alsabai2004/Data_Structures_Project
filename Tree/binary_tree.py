class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size += 1
            return True

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    self.size += 1
                    return True

                current = current.left

            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    self.size += 1
                    return True

                current = current.right

            else:
                return False

    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return True

            if data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def contains(self, data):
        return self.search(data)

    def inorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            result.append(node.data)
            traverse(node.right)

        traverse(self.root)
        return result

    def preorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            result.append(node.data)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return result

    def postorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            traverse(node.right)
            result.append(node.data)

        traverse(self.root)
        return result

    def levelorder(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]
        index = 0

        while index < len(queue):
            node = queue[index]
            index += 1

            result.append(node.data)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return result

    def find_min(self):
        if self.root is None:
            return None

        node = self._get_min_node(self.root)
        return node.data

    def find_max(self):
        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.data

    def _get_min_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def _get_max_node(self, node):
        current = node

        while current.right is not None:
            current = current.right

        return current

    def height(self):
        def calculate(node):
            if node is None:
                return -1

            left_height = calculate(node.left)
            right_height = calculate(node.right)

            return 1 + max(left_height, right_height)

        return calculate(self.root)

    def delete(self, data):
        if not self.search(data):
            return False

        self.root = self._delete(self.root, data)
        self.size -= 1

        return True

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)

        elif data > node.data:
            node.right = self._delete(node.right, data)

        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self._get_min_node(node.right)
            node.data = successor.data
            node.right = self._delete(node.right, successor.data)

        return node

    def is_empty(self):
        return self.root is None

    def get_size(self):
        return self.size

    def count(self):
        return self.size

    def clear(self):
        self.root = None
        self.size = 0

    def display(self):
        if self.root is None:
            print("Tree is empty.")
            return

        self._display(self.root, "", True)

    def _display(self, node, prefix, is_left):
        if node.right is not None:
            self._display(
                node.right,
                prefix + ("│   " if is_left else "    "),
                False
            )

        print(
            prefix
            + ("└── " if is_left else "┌── ")
            + str(node.data)
        )

        if node.left is not None:
            self._display(
                node.left,
                prefix + ("    " if is_left else "│   "),
                True
            )

    def to_list(self):
        return self.inorder()

    def __len__(self):
        return self.size
