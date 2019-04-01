import unittest

from helpers.quick_sort import QuickSort


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.sort = QuickSort()

    def test_quick_sort_with_empty_list(self):
        self.assertEqual([], self.sort.sort_list([]))

    def test_quick_sort_with_one_element(self):
        self.assertEqual([1], self.sort.sort_list([1]))
        self.assertEqual([10], self.sort.sort_list([10]))

    def test_quick_sort(self):
        self.assertEqual([1, 2, 3], self.sort.sort_list([3, 2, 1]))
        self.assertEqual([1, 2, 2, 3, 3], self.sort.sort_list([3, 2, 1, 2, 3]))
        self.assertEqual([-1, 2, 2, 3, 3], self.sort.sort_list([3, 2, -1, 2, 3]))

    def test_quick_sort_with_big_list(self):
        big_list = [0] * 500
        self.assertEqual(big_list, self.sort.sort_list(big_list))

    def test_quick_sort_with_huge_list(self):
        MAX_SIZE_ARRAY = 900
        raise_list = [0] * (MAX_SIZE_ARRAY + 1)
        not_raise_list = [0] * MAX_SIZE_ARRAY
        self.assertRaises(RecursionError, self.sort.sort_list, raise_list)
        self.assertEqual(not_raise_list, self.sort.sort_list(not_raise_list))