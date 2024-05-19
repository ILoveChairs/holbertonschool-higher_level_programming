#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None or not isinstance(next_node, Node):
            rase TypeError("next_node must be a Node object")
        self.__next_node = next_node
    @property
    def data(self):
        return self.__data
    @property
    def next_node(self):
        return self.__next_node
    @data.setter
    def data(self, value):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
    @next_node.setter
    def next_node(self, value):
        if next_node is not None or not isinstance(next_node, Node):
            rase TypeError("next_node must be a Node object")
        self.__next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        if self.__head is None:
            self.head = new Node(value)
            return
        current = self.__head
        while current is not None:
            if current.data > value:
                new_node = new Node(value)
                return
            current = current.next_node
        self.__head = new Node(value)
    def __str__(self):
        current = self.__head
        while current is not None:
            print(current)
            current = current.next_node
