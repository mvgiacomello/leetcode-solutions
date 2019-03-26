import unittest

from helpers.linked_list import LinkedListNode as llist
from merge_two_sorted_lists import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual([1, 1, 2, 3, 4, 4],
                         llist.to_list(solution.merge_two_lists(llist.from_list([1, 2, 4]),
                                                                llist.from_list([1, 3, 4]))))
        self.assertEqual([],
                         llist.to_list(solution.merge_two_lists(llist.from_list([]),
                                                                llist.from_list([]))))
        self.assertEqual([1],
                         llist.to_list(solution.merge_two_lists(llist.from_list([1]),
                                                                llist.from_list([]))))
        self.assertEqual([1],
                         llist.to_list(solution.merge_two_lists(llist.from_list([]),
                                                                llist.from_list([1]))))
        self.assertEqual([-1],
                         llist.to_list(solution.merge_two_lists(llist.from_list([-1]),
                                                                llist.from_list([]))))
        self.assertEqual([-1],
                         llist.to_list(solution.merge_two_lists(llist.from_list([]),
                                                                llist.from_list([-1]))))
        self.assertEqual([1, 1, 1, 1, 1],
                         llist.to_list(solution.merge_two_lists(llist.from_list([1, 1, 1, 1, 1]),
                                                                llist.from_list([]))))
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         llist.to_list(solution.merge_two_lists(llist.from_list([1, 1, 1, 1, 1]),
                                                                llist.from_list([1, 1, 1, 1, 1]))))


if __name__ == '__main__':
    unittest.main()
