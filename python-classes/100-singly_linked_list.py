#!/usr/bin/python3
'''Node:
    SLL node.
    SinglLinkedList:
    SLL
'''


class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
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
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''
        __head(Node): First Node
    '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            return
        prev = None
        current = self.__head
        while current is not None:
            if current.data > value:
                new_node = Node(value, current)
                if prev is None:
                    self.__head = new_node
                else:
                    prev.next_node = new_node
                return
            prev = current
            current = current.next_node
        prev.next_node = Node(value)

    def __str__(self):
        output = []
        current = self.__head
        while current is not None:
            output.append(str(current.data))
            current = current.next_node
        return "\n".join(output)
