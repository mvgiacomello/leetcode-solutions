import unittest

from number_of_islands.solution import Solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(0, Solution().num_islands(
            None))
        self.assertEqual(0, Solution().num_islands(
            [[]]))
        self.assertEqual(1, Solution().num_islands(
            [['1']]))
        self.assertEqual(2, Solution().num_islands(
            [['1', '0'],
             ['0', '1']]))
        self.assertEqual(1, Solution().num_islands(
            [['1', '1'],
             ['0', '1']]))
        self.assertEqual(1, Solution().num_islands(
            [['1', '0'],
             ['1', '1']]))
        self.assertEqual(1, Solution().num_islands(
            [['1', '1'],
             ['1', '1']]))
        self.assertEqual(1, Solution().num_islands(
            [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]))
        self.assertEqual(3, Solution().num_islands(
            [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]))
        self.assertEqual(3, Solution().num_islands(
            [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["1", "1", "0", "1", "0"],
             ["0", "0", "0", "0", "1"]]))
        self.assertEqual(1, Solution().num_islands(
            [["1", "1", "1", "1", "1"],
             ["1", "1", "1", "1", "1"],
             ["1", "1", "1", "1", "1"],
             ["1", "1", "1", "1", "1"]]))
        self.assertEqual(0, Solution().num_islands(
            [["0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]))
        self.assertEqual(13, Solution().num_islands(
            [["1", "0", "1", "0", "1"],
             ["0", "1", "0", "1", "0"],
             ["1", "0", "1", "0", "1"],
             ["0", "1", "0", "1", "0"],
             ["1", "0", "1", "0", "1"]]))
        self.assertEqual(3, Solution().num_islands(
            [['1'],
             ['0'],
             ['1'],
             ['0'],
             ['1'],
             ['0']]))

if __name__ == '__main__':
    unittest.main()
