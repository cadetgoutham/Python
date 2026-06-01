"""
Singly Linked List with Interactive Menu

Description:
    A self-contained object-oriented implementation of a Singly Linked List.
    Supports dynamic memory node configurations including sequential insertions,
    positional indexing operations, linear searching, and node popping.

Output Preview:
    --- Linked List Menu ---
    1. Push (add to end)
    ...
    Select an operation (1-7): 1
    Enter value to push: 10
    Pushed 10 to the list.
    Linked List: 10 -> None

How to Run:
    $ python linked_list.py
"""

class ListNode:
    """Represents an isolated data element container pointing to its successor."""
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    """Manages node tracking states, indices, and list transformations."""
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, new_data):
        """Appends a node containing new_data to the end of the list structure."""
        new_node = ListNode(new_data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

        self.count += 1

    def pop(self):
        """Removes the final element node, returning its raw data value."""
        if self.head is None:
            print("List is empty, nothing to pop.")
            return None

        # Handle a single-element list boundary case
        if self.head.next is None:
            extracted_val = self.head.data
            self.head = None
            self.count -= 1
            return extracted_val

        # Locate the second-to-last node elements
        previous_node = None
        current_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        extracted_val = current_node.data
        previous_node.next = None
        self.count -= 1
        return extracted_val

    def insert(self, position, new_data):
        """Inserts a new node at a given 1-based index position boundary."""
        if position < 1 or position > self.count + 1:
            print(f"Invalid position. Valid range: 1 to {self.count + 1}")
            return

        new_node = ListNode(new_data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(position - 2):
                current_node = current_node.next
            
            new_node.next = current_node.next
            current_node.next = new_node

        self.count += 1

    def remove(self, position):
        """Extracts and removes a targeted node via a 1-based index position."""
        if self.head is None:
            print("List is empty, nothing to remove.")
            return None

        if position < 1 or position > self.count:
            print(f"Invalid position. Valid range: 1 to {self.count}")
            return None

        if position == 1:
            extracted_val = self.head.data
            self.head = self.head.next
            self.count -= 1
            return extracted_val

        current_node = self.head
        for _ in range(position - 2):
            current_node = current_node.next

        extracted_val = current_node.next.data
        current_node.next = current_node.next.next
        self.count -= 1
        return extracted_val

    def search(self, target_data):
        """Iterates lineally to return the 1-based index match, or -1 if absent."""
        current_node = self.head
        current_index = 1
        while current_node:
            if current_node.data == target_data:
                return current_index
            current_node = current_node.next
            current_index += 1
        return -1

    def print_list(self):
        """Outputs structural nodes sequentially into a legible data layout map."""
        if self.head is None:
            print("Linked list state: Empty")
            return
        
        current_node = self.head
        print("Linked List: ", end="")
        while current_node:
            print(f"{current_node.data} -> ", end="")
            current_node = current_node.next
        print("None")


def display_terminal_menu():
    """Displays standard user execution operational instructions."""
    print("\n--- Linked List Menu ---")
    print("1. Push (add to end)")
    print("2. Pop (remove from end)")
    print("3. Insert at position")
    print("4. Remove at position")
    print("5. Search for a value")
    print("6. Print list")
    print("7. Exit")


def main():
    linked_list = LinkedList()

    while True:
        display_terminal_menu()
        try:
            choice = int(input("Select an operation (1-7): "))
        except ValueError:
            print("Please enter a valid choice integer.")
            continue

        if choice == 7:
            print("Exiting runtime context...")
            break

        if choice == 1:
            try:
                val = int(input("Enter integer value to push: "))
                linked_list.push(val)
                print(f"Pushed {val} to the list.")
                linked_list.print_list()
            except ValueError:
                print("Invalid data item framework. Integers only.")

        elif choice == 2:
            popped_value = linked_list.pop()
            if popped_value is not None:
                print(f"Popped value: {popped_value}")
                linked_list.print_list()

        elif choice == 3:
            try:
                pos = int(input(f"Enter target insertion location (1 to {linked_list.count + 1}): "))
                val = int(input("Enter integer value to insert: "))
                linked_list.insert(pos, val)
                print(f"Inserted {val} at position {pos}.")
                linked_list.print_list()
            except ValueError:
                print("Invalid input sequence parameters.")

        elif choice == 4:
            try:
                pos = int(input(f"Enter deletion position (1 to {linked_list.count}): "))
                removed_value = linked_list.remove(pos)
                if removed_value is not None:
                    print(f"Removed value: {removed_value}")
                    linked_list.print_list()
            except ValueError:
                print("Invalid positional input parameter format.")

        elif choice == 5:
            try:
                val = int(input("Enter search lookup value: "))
                found_index = linked_list.search(val)
                if found_index != -1:
                    print(f"Value {val} localized at element position: {found_index}.")
                else:
                    print(f"Value {val} was not identified across current instances.")
            except ValueError:
                print("Search queries require valid integer parameters.")

        elif choice == 6:
            linked_list.print_list()
        else:
            print("Selection out of bounds. Boundaries are limited between 1 and 7.")


if __name__ == "__main__":
    main()