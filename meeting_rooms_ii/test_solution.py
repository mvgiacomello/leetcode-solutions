import unittest

from meeting_rooms_ii import solution
from meeting_rooms_ii.interval import Interval


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(2, solution.min_meeting_rooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
        self.assertEqual(1, solution.min_meeting_rooms([Interval(7, 10), Interval(2, 4)]))
        self.assertEqual(0, solution.min_meeting_rooms([]))
        self.assertEqual(1, solution.min_meeting_rooms([Interval(7, 10)]))


if __name__ == '__main__':
    unittest.main()
