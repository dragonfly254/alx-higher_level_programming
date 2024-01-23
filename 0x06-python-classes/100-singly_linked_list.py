#!/usr/bin/python3
"""This module provides access to node and singly linked list class

It contains class node for creating the nodes of the list and
class singly linked list for creatining the list.

this file can be im[orted as amodule and has the follwing
functions:
    *insert_sorted - inserts the node into the sorted linked list.
"""


class Node:
    """creates a node.

    attributes:
        __data (int): data to be store in the list.
        __next_node (Node): the following node in the list.
    """
    def __init__(self, data, next_node=None):
        """node initializer.

        Args:
            data (int): data stored in the node
            next_node (Node): next node in the list.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns next_node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """sets the value of data.

        Args:
            value: the value of the data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """sets the value of the node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """create a singly linked list"""
    def __init__(self):
        """initializes the list"""
        self.__head = None

    def __str__(self):
        """prints the list"""
        stri = ""
        temp = self.__head
        while (temp):
            stri = stri + str(temp.data)
            if (temp.next_node):
                stri = stri + "\n"
            temp = temp.next_node
        return stri

    def sorted_insert(self, value):
        """inserts the node in sorted order"""
        if not self.__head:
            self.__head = Node(value, None)

        else:
            aux1 = self.__head
            aux2 = aux1.next_node
            if (self.__head.data > value):
                self.__head = Node(value, self.__head)
            else:
                while (aux2):
                    if (aux2.data > value):
                        new = Node(value, None)
                        new.next_node = aux2
                        aux1.next_node = new
                        break
                    aux1 = aux1.next_node
                    aux2 = aux2.next_node
                new = Node(value, aux2)
                aux1.next_node = new
