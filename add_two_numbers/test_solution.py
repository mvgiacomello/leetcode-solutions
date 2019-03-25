import unittest
from add_two_numbers import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual([2], solution.add_two_numbers([1], [1]))
        self.assertEqual([3, 4, 5], solution.add_two_numbers([1, 1, 1], [4, 3, 2]))
        self.assertEqual([1, 0, 0, 0], solution.add_two_numbers([1], [9, 9, 9, ]))
        with self.assertRaises(ValueError):
            self.assertEqual([0], solution.add_two_numbers([1], [-1]))
            self.assertEqual([-1], solution.add_two_numbers([1], [-2]))
            self.assertEqual([0], solution.add_two_numbers([0], [1]))
            self.assertEqual([], solution.add_two_numbers([], []))


if __name__ == '__main__':
    unittest.main()
