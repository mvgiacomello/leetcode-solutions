import unittest
from longest_substring_wo_repeat_chars import solution


class TestSolution(unittest.TestCase):
    def test_repeat_char_detection(self):
        self.assertTrue(solution.repeat_chars('aa'))
        self.assertTrue(solution.repeat_chars('aA'))
        self.assertTrue(solution.repeat_chars('abcabcd'))
        self.assertFalse(solution.repeat_chars('ab'))
        self.assertFalse(solution.repeat_chars('abc'))

    def test_solution(self):
        self.assertEqual(0, solution.length_longest_substring(''))
        self.assertEqual(1, solution.length_longest_substring('a'))
        self.assertEqual(2, solution.length_longest_substring('au'))
        self.assertEqual(1, solution.length_longest_substring('aa'))
        self.assertEqual(2, solution.length_longest_substring('aab'))
        self.assertEqual(3, solution.length_longest_substring('abcabcbb'))
        self.assertEqual(3, solution.length_longest_substring('abcABCBB'))
        self.assertEqual(1, solution.length_longest_substring('bbbbb'))
        self.assertEqual(3, solution.length_longest_substring('pwwkew'))
        self.assertEqual(6, solution.length_longest_substring('mauricio'))

if __name__ == '__main__':
    unittest.main()
