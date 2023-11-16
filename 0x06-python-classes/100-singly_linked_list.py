#!/usr/bin/python3
"""
Define a class Node and SinglyLinkedList.
"""


class Node:
    """
    Represent a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the linked list.

        Raises:
            TypeError: If data is not an integer, or next_node is not a Node object.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the node.

        Returns:
            int: The data of the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If data is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If next_node is not a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represent a singly linked list.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList instance.

        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value of the new Node.

        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.

        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
