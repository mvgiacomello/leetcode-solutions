import unittest
from two_sum import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution.two_sum(nums=[2, 7, 11, 3], target=9), [0, 1])
        self.assertEqual(solution.two_sum(nums=[7, 2, 11, 3], target=9), [0, 1])
        self.assertEqual(solution.two_sum(nums=[7, 2, 11, 3], target=14), [2, 3])
        self.assertEqual(solution.two_sum(nums=[-1, -2, 11, 3], target=-3), [0, 1])
        self.assertEqual(solution.two_sum(nums=[-1, -2, -1, -2], target=-3), [0, 1])
        self.assertEqual(solution.two_sum(nums=[0, 0, 0, 0], target=0), [0, 1])
        self.assertEqual(solution.two_sum(nums=[7, 2, 11, 3], target=9), [0, 1])
        with self.assertRaises(ValueError):
            solution.two_sum(nums=[7], target=7)
            solution.two_sum(nums=[1, 2, 3], target=8)


if __name__ == '__main__':
    unittest.main()
