import unittest
from typing import Any


class LinkedList:
    def __init__(self):
        self.size = 0
        self._first = self._last = None

    def add(self, value: Any):
        """
        :param value: value of append at the end of the linked list
        """
        new_node = _LinkedListNode(value)
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


class _LinkedListNode:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class _TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_add_and_size(self):
        self.linked_list.add(1)
        self.assertEqual(1, self.linked_list.size)
        self.linked_list.add(2)
        self.assertEqual(2, self.linked_list.size)
        self.linked_list.add(3)
        self.assertEqual(3, self.linked_list.size)
        self.linked_list.add(4)
        self.assertEqual(4, self.linked_list.size)

    def test_add_and_get(self):
        self.linked_list.add(1)
        self.assertEqual(1, self.linked_list.get(0))
        self.linked_list.add(2)
        self.assertEqual(1, self.linked_list.get(0))
        self.assertEqual(2, self.linked_list.get(1))
        self.linked_list.add(3)
        self.assertEqual(1, self.linked_list.get(0))
        self.assertEqual(2, self.linked_list.get(1))
        self.assertEqual(3, self.linked_list.get(2))
        self.linked_list.add(4)
        self.assertEqual(1, self.linked_list.get(0))
        self.assertEqual(2, self.linked_list.get(1))
        self.assertEqual(3, self.linked_list.get(2))
        self.assertEqual(4, self.linked_list.get(3))

    def test_remove_with_one_element(self):
        self.linked_list.add(1)
        self.linked_list.remove(0)
        self.assertEqual(0, self.linked_list.size)

    def test_remove_first_with_two_elements(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.remove(0)
        self.assertEqual(1, self.linked_list.size)
        self.assertEqual(2, self.linked_list.get(0))

    def test_remove_second_with_two_elements(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.remove(self.linked_list.size - 1)
        self.assertEqual(1, self.linked_list.size)
        self.assertEqual(1, self.linked_list.get(0))

    def test_remove_first_with_three_elements(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove(0)
        self.assertEqual(2, self.linked_list.size)
        self.assertEqual(2, self.linked_list.get(0))
        self.assertEqual(3, self.linked_list.get(1))

    def test_remove_second_with_three_elements(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove(1)
        self.assertEqual(2, self.linked_list.size)
        self.assertEqual(1, self.linked_list.get(0))
        self.assertEqual(3, self.linked_list.get(1))

    def test_remove_third_with_three_elements(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.remove(2)
        self.assertEqual(2, self.linked_list.size)
        self.assertEqual(1, self.linked_list.get(0))
        self.assertEqual(2, self.linked_list.get(1))

    def test_remove_bigger_list(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.add(4)
        self.linked_list.add(5)
        self.linked_list.add(6)
        self.linked_list.remove(4)
        self.assertEqual(5, self.linked_list.size)
        self.assertEqual(3, self.linked_list.get(2))
        self.assertEqual(4, self.linked_list.get(3))
        self.assertEqual(6, self.linked_list.get(4))

    def test_from_four_to_zero_remove_first(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.add(4)
        self.linked_list.remove(0)
        self.assertEqual(3, self.linked_list.size)
        self.linked_list.remove(0)
        self.assertEqual(2, self.linked_list.size)
        self.linked_list.remove(0)
        self.assertEqual(1, self.linked_list.size)
        self.linked_list.remove(0)
        self.assertEqual(0, self.linked_list.size)

    def test_from_four_to_zero_remove_last(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.add(4)
        self.linked_list.remove(self.linked_list.size - 1)
        self.assertEqual(3, self.linked_list.size)
        self.linked_list.remove(self.linked_list.size - 1)
        self.assertEqual(2, self.linked_list.size)
        self.linked_list.remove(self.linked_list.size - 1)
        self.assertEqual(1, self.linked_list.size)
        self.linked_list.remove(0)
        self.assertEqual(0, self.linked_list.size)

    def test_from_four_to_zero_remove_second(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.add(4)
        self.linked_list.remove(1)
        self.assertEqual(3, self.linked_list.size)
        self.linked_list.remove(1)
        self.assertEqual(2, self.linked_list.size)
        self.linked_list.remove(1)
        self.assertEqual(1, self.linked_list.size)
        self.linked_list.remove(0)
        self.assertEqual(0, self.linked_list.size)
