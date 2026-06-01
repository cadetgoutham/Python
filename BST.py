"""
Binary Search Tree (BST) with Interactive Menu

Description:
    A self-contained object-oriented implementation of a Binary Search Tree.
    Supports recursive insertion, complex node deletion (0, 1, or 2 children),
    $O(\log n)$ searching, and three depth-first traversal strategies.

Output Preview:
    --- BST Menu ---
    1. Add value
    ...
    Select an operation (1-7): 1
    Enter value to add: 50
    Added: 50

How to Run:
    $ python binary_search_tree.py
"""

class TreeNode:
    """Represents a single structural node within the Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Manages root states and recursive execution branches of the BST."""
    def __init__(self):
        self.root = None

    def _insert(self, data, current_node):
        """Recursively guides data to its appropriate leaf position."""
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
                print(f"Added: {data}")
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
                print(f"Added: {data}")
            else:
                self._insert(data, current_node.right)
        else:
            print(f"Value {data} already exists in the tree.")

    def add(self, data):
        """Public insertion access point."""
        if self.root is None:
            self.root = TreeNode(data)
            print(f"Added: {data} as root.")
        else:
            self._insert(data, self.root)

    def _delete_node(self, node, data):
        """Handles structural re-linking operations during node removal."""
        if node is None:
            print(f"Value {data} not found in the tree.")
            return node

        if data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            # Case 1 & 2: Single child or Leaf Node closures
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3: Node with two children. Seek In-Order Successor.
            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.data = successor.data
            node.right = self._delete_node(node.right, successor.data)

        return node

    def delete(self, data):
        """Public deletion access point."""
        self.root = self._delete_node(self.root, data)

    def _search_node(self, data, node):
        """Tracks nodes down specific computational paths looking for a match."""
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_node(data, node.left)
        else:
            return self._search_node(data, node.right)

    def search(self, data):
        """Public searching access point using a safe decoupled boundary."""
        return self._search_node(data, self.root)

    def in_order(self, node):
        """Left -> Root -> Right traversal pattern."""
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def pre_order(self, node):
        """Root -> Left -> Right traversal pattern."""
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        """Left -> Right -> Root traversal pattern."""
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")


def print_menu():
    """Displays standard terminal interface options."""
    print("\n--- BST Menu ---")
    print("1. Add value")
    print("2. Delete value")
    print("3. Search value")
    print("4. In-order traversal (sorted)")
    print("5. Pre-order traversal")
    print("6. Post-order traversal")
    print("7. Exit")


def main():
    tree = BinarySearchTree()

    while True:
        print_menu()
        try:
            choice = int(input("Select an operation (1-7): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 7:
            print("Exiting...")
            break

        if choice in [1, 2, 3]:
            try:
                val = int(input("Enter target integer value: "))
            except ValueError:
                print("Invalid configuration. Action requires an integer.")
                continue

            if choice == 1:
                tree.add(val)
            elif choice == 2:
                tree.delete(val)
                print(f"Removal process evaluated for: {val}")
            elif choice == 3:
                found = tree.search(val)
                print(f"Value {val} {'found' if found else 'not found'} in tree.")

        elif choice in [4, 5, 6]:
            if tree.root is None:
                print("Tree is currently empty.")
                continue

            if choice == 4:
                print("In-order: ", end="")
                tree.in_order(tree.root)
            elif choice == 5:
                print("Pre-order: ", end="")
                tree.pre_order(tree.root)
            elif choice == 6:
                print("Post-order: ", end="")
                tree.post_order(tree.root)
            print()
        else:
            print("Out of bounds selection. Range parameters are strictly 1-7.")


if __name__ == "__main__":
    main()