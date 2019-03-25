import unittest
from longest_substring_wo_repeat_chars import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(0, solution.length_longest_substring(''))
        self.assertEqual(1, solution.length_longest_substring('a'))
        self.assertEqual(3, solution.length_longest_substring('abcabcbb'))
        self.assertEqual(3, solution.length_longest_substring('abcABCBB'))
        self.assertEqual(1, solution.length_longest_substring('bbbbb'))
        self.assertEqual(3, solution.length_longest_substring('pwwkew'))
        self.assertEqual(6, solution.length_longest_substring('mauricio'))


if __name__ == '__main__':
    unittest.main()
