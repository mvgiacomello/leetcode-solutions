import unittest

from helpers.linked_list import LinkedListNode as llist
from reverse_linked_list import solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.list_in_order = []
        for value in range(0, 100000):
            self.list_in_order.append(value)
        self.list_in_reverse = self.list_in_order.copy()
        self.list_in_reverse.sort(reverse=True)

    def test_solution(self):
        self.assertEqual(None, solution.reverse_list(None))
        self.assertEqual(llist(5), solution.reverse_list(llist(5)))
        self.assertEqual(llist(5).set_next(llist(4)), solution.reverse_list(llist(4).set_next(llist(5))))
        self.assertEqual(self.list_in_reverse,
                         llist.to_list(solution.reverse_list(llist.from_list(self.list_in_order))))


if __name__ == '__main__':
    unittest.main()
