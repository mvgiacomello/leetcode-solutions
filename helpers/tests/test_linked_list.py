import unittest

from helpers.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
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

    def test_pop(self):
        self.linked_list.add(1)
        self.assertEqual(1, self.linked_list.pop(0))
        self.assertEqual(0, self.linked_list.size)

    def test_raises_when_get(self):
        self.assertRaises(IndexError, self.linked_list.get, -1)
        self.assertRaises(IndexError, self.linked_list.get, 0)
        self.assertRaises(IndexError, self.linked_list.get, 1)
        self.linked_list.add(1)
        self.assertRaises(IndexError, self.linked_list.get, 1)

    def test_raises_when_remove(self):
        self.assertRaises(IndexError, self.linked_list.remove, -1)
        self.assertRaises(IndexError, self.linked_list.remove, 0)
        self.assertRaises(IndexError, self.linked_list.remove, 1)
        self.linked_list.add(1)
        self.assertRaises(IndexError, self.linked_list.remove, 1)

    def test_raises_when_pop(self):
        self.assertRaises(IndexError, self.linked_list.pop, -1)
        self.assertRaises(IndexError, self.linked_list.pop, 0)
        self.assertRaises(IndexError, self.linked_list.pop, 1)
        self.linked_list.add(1)
        self.assertRaises(IndexError, self.linked_list.pop, 1)


if __name__ == '__main__':
    unittest.main()
