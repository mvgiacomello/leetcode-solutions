import unittest
from three_sum import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual([], solution.three_sum([]))
        self.assertEqual([], solution.three_sum([0]))
        self.assertEqual([[0, 0, 0]], solution.three_sum([0, 0, 0, 0]))
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], solution.three_sum([-1, 0, 1, 2, -1, -4]))
        self.assertEqual([[-15, 1, 14], [-15, 2, 13], [-15, 3, 12], [-15, 4, 11], [-15, 5, 10], [-15, 6, 9],
                          [-15, 7, 8], [-14, 0, 14], [-14, 1, 13], [-14, 2, 12], [-14, 3, 11], [-14, 4, 10],
                          [-14, 5, 9], [-14, 6, 8], [-14, 7, 7], [-13, -1, 14], [-13, 0, 13], [-13, 1, 12],
                          [-13, 2, 11], [-13, 3, 10], [-13, 4, 9], [-13, 5, 8], [-13, 6, 7], [-12, -2, 14],
                          [-12, -1, 13], [-12, 0, 12], [-12, 1, 11], [-12, 2, 10], [-12, 3, 9], [-12, 4, 8],
                          [-12, 5, 7], [-12, 6, 6], [-11, -3, 14], [-11, -2, 13], [-11, -1, 12], [-11, 0, 11],
                          [-11, 1, 10], [-11, 2, 9], [-11, 3, 8], [-11, 4, 7], [-11, 5, 6], [-10, -4, 14],
                          [-10, -3, 13], [-10, -2, 12], [-10, -1, 11], [-10, 0, 10], [-10, 1, 9], [-10, 2, 8],
                          [-10, 3, 7], [-10, 4, 6], [-10, 5, 5], [-9, -5, 14], [-9, -4, 13], [-9, -3, 12],
                          [-9, -2, 11], [-9, -1, 10], [-9, 0, 9], [-9, 1, 8], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5],
                          [-8, -6, 14], [-8, -5, 13], [-8, -4, 12], [-8, -3, 11], [-8, -2, 10], [-8, -1, 9],
                          [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-8, 4, 4], [-7, -7, 14], [-7, -6, 13],
                          [-7, -5, 12], [-7, -4, 11], [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], [-7, 0, 7], [-7, 1, 6],
                          [-7, 2, 5], [-7, 3, 4], [-6, -6, 12], [-6, -5, 11], [-6, -4, 10], [-6, -3, 9], [-6, -2, 8],
                          [-6, -1, 7], [-6, 0, 6], [-6, 1, 5], [-6, 2, 4], [-6, 3, 3], [-5, -5, 10], [-5, -4, 9],
                          [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -4, 8],
                          [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-3, -3, 6],
                          [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2],
                          [-1, -1, 2], [-1, 0, 1]], solution.three_sum(
            [-14, -3, 11, -3, 12, -1, 11, 13, 5, 6, -11, -14, -6, 11, -4, -15, 3, -15, 9, -10, 13, -10, -9, -13, -12,
             12, -7, 12, 12, 3, 9, 5, -14, -3, 9, 13, 11, 5, 3, -6, -12, -1, -5, -3, -4, -2, -10, 6, -10, 14, 3, -11,
             11, 10, -9, 7, -1, -9, 4, -12, 2, -2, 8, 3, 3, -6, -7, -1, 6, 12, 8, 9, -12, 10, -8, -1, -7, -3, 12, -9,
             -12, 1, -5, 6, -12, -7, -2, 2, -8, -13, 5, 9, -7, -10, -3, 11, -1, -3, -13, -10, -14, 11, 6, -10, 6, 13, 4,
             7, -13, -6, 13, 12, 10, -15, 4, 13, -7, 9, -8, 0, 4, 4, -6, 12, 9, -2, 0]))


if __name__ == '__main__':
    unittest.main()