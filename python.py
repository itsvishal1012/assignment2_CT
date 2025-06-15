class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to manage the singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """Print the entire list."""
        current_node = self.head
        if not current_node:
            print("The list is empty.")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        
        if n < 1:
            raise Exception("Index must be a positive integer.")
        
        current_node = self.head
        
        # If the head needs to be removed
        if n == 1:
            self.head = current_node.next
            return
        
        # Find the previous node of the node to be deleted
        for _ in range(n - 2):
            current_node = current_node.next
            if current_node is None:
                raise Exception("Index out of range.")
        
        # If current_node is None, then the index is out of range
        if current_node is None or current_node.next is None:
            raise Exception("Index out of range.")
        
        # Node current_node.next is the node to be deleted
        current_node.next = current_node.next.next


def main():
    linked_list = LinkedList()
    
    print("Singly Linked List Interactive Program")
    print("Commands:")
    print("1: Add a node")
    print("2: Print the list")
    print("3: Delete the nth node")
    print("4: Exit")

    while True:
        try:
            choice = input("\nEnter command number (1-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program.")
            break
        
        if choice == "1":
            value = input("Enter value to add to the list: ").strip()
            if value == "":
                print("Empty input is not allowed.")
                continue
            linked_list.add_node(value)
            print(f"Added node with value: {value}")
        
        elif choice == "2":
            print("Current List:")
            linked_list.print_list()

        elif choice == "3":
            if linked_list.head is None:
                print("YOu Cannot delete from an empty list.")
                continue
            index_str = input("Enter the 1-based index of the node to delete: ").strip()
            if not index_str.isdigit():
                print("Index must be a positive integer.")
                continue
            index = int(index_str)
            try:
                linked_list.delete_nth_node(index)
                print(f"Deleted node at position {index}.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            print("Exiting program.")
            break
        
        else:
            print("You entered an Invalid command. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
