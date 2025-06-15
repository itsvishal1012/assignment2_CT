# assignment2_CT
## Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list.

# Singly Linked List Implementation in Python
This project provides a comprehensive implementation of a singly linked list data structure using Object-Oriented Programming (OOP) principles in Python. It includes a Node class for individual elements and a LinkedList class for managing the list, along with methods for common operations like adding, printing, and deleting nodes. Robust error handling is integrated to manage edge cases.

# Features:
1.) Node Class: Represents a single element in the linked list, holding data and a reference to the next node.

2.) LinkedList Class: Manages the collection of Node objects.

3.) append(data): Adds a new node with the given data to the end of the list.

4.) print_list(): Traverses the list from head to tail and prints all elements.

5.) delete_node(n): Deletes the node at a specified 1-based index n.

# Exception Handling:

Prevents deletion from an empty list.

Handles attempts to delete a node with an index that is out of the list's bounds.

Validates that the provided index n is a positive integer.

How to Run
Save the Code: Save the Python code provided above into a file named python.py

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved python.py, and run the script:

python python.py
