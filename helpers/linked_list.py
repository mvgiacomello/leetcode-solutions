import warnings
from typing import Any, List


class LinkedList:
    def __init__(self):
        self.size = 0
        self._first = self._last = None

    @property
    def head(self) -> 'LinkedListNode':
        """
        :return: the element at position '0'
        """
        return self._first

    @property
    def tail(self) -> 'LinkedListNode':
        """
        :return: the element at position size - 1
        """
        return self._last

    def add(self, value: Any):
        """
        :param value: value of append at the end of the linked list
        """
        new_node = LinkedListNode(value)
        if self._first is None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self.size += 1

    def remove(self, index: int):
        """
        :param index: index in the linked lest to remove. Starts from 0
        :raises: IndexError if index provided is below 0 or above size of the linked list
        """
        if index >= self.size or index < 0:
            raise IndexError('Value of index provided should be between zero and {}'.format(self.size - 1))

        if self.size == 1:
            self._first = self._last = None

        elif self.size == 2:
            if index == 0:
                self._first = self._last
            if index == 1:
                self._last = self._first
            self._first.next = None

        else:
            if index == 0:
                self._first = self._first.next
            else:
                temp = 1
                previous_node = self._first
                index_node = self._first.next
                next_node = self._first.next.next
                while temp != index:
                    # Keep walking through the linked list until index is reached
                    previous_node = previous_node.next
                    index_node = index_node.next
                    next_node = next_node.next
                    temp += 1
                previous_node.next = next_node
                if previous_node.next is None:
                    self._last = previous_node

        self.size -= 1

    def get(self, index: int) -> Any:
        """
        :param index: index in the linked lest to retrieve. Starts from 0
        :return: the value that element
        :raises: IndexError if index provided is below 0 or above size of the linked list
        """
        if index >= self.size or index < 0:
            raise IndexError('Value of index provided should be between zero and {}'.format(self.size - 1))
        if self.size == 0:
            return None
        elif self.size == 1 and index == 0:
            return self._first.value
        elif self.size == 2 and index == 1:
            return self._last.value
        else:
            temp = 0
            node = self._first
            while temp != index:
                node = node.next
                temp += 1
            return node.value

    def pop(self, index) -> Any:
        """
        :param index: index in the linked lest to retrieve and remove. Starts from 0
        :return: the value that element
        """
        value = self.get(index)
        self.remove(index)
        return value


class LinkedListNode:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

    def set_next(self, next: 'LinkedListNode'):
        """
        Useful for writing a list in one line (mostly for LeetCode solutions)
        :param next: the next element
        """
        warnings.warn('Use set_next only for 1:1 solutions of LeetCode')
        self.next = next

    @classmethod
    def from_list(cls, list: List) -> 'LinkedListNode':
        """
        :param list: a list representing the chain
        :return: the first node of a chain of LinkedListNode
        """
        warnings.warn('Use from_list only for 1:1 solutions of LeetCode')
        node = LinkedListNode(-1)
        previous = node
        for entry in list:
            previous.next = LinkedListNode(entry)
            previous = previous.next
        return node.next

    @classmethod
    def to_list(cls, node: 'LinkedListNode') -> List:
        """
        :param node: the first node of a chain of LinkedListNode
        :return: a list representing the chain
        """
        warnings.warn('Use to_list only for 1:1 solutions of LeetCode')
        list = []
        while node is not None:
            list.append(node.value)
            node = node.next
        return list
