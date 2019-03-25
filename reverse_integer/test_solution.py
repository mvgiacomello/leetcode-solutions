import unittest
from reverse_integer import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(321, solution.reverse(123))
        self.assertEqual(-321, solution.reverse(-123))
        self.assertEqual(21, solution.reverse(120))
        self.assertEqual(0, solution.reverse(1534236469))
        self.assertEqual(0, solution.reverse(-(2 ** 31)))
        self.assertEqual(0, solution.reverse((2 ** 31)))


if __name__ == '__main__':
    unittest.main()
