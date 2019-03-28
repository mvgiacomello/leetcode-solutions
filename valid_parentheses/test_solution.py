import unittest
from valid_parentheses import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(solution.is_valid(''))
        self.assertFalse(solution.is_valid(']'))
        self.assertFalse(solution.is_valid(')'))
        self.assertFalse(solution.is_valid('}'))
        self.assertFalse(solution.is_valid('('))
        self.assertFalse(solution.is_valid('['))
        self.assertFalse(solution.is_valid('{'))
        self.assertTrue(solution.is_valid('()'))
        self.assertTrue(solution.is_valid('[]'))
        self.assertTrue(solution.is_valid('{}'))
        self.assertTrue(solution.is_valid('()[]{}'))
        self.assertTrue(solution.is_valid('([])'))
        self.assertTrue(solution.is_valid('([{}])'))
        self.assertFalse(solution.is_valid('([)]'))


if __name__ == '__main__':
    unittest.main()
