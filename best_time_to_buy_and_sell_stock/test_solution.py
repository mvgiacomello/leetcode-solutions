import unittest
import math
import random

from best_time_to_buy_and_sell_stock import solution


class TestSolution(unittest.TestCase):

    def test_solution_edge_cases(self):
        self.assertEqual(math.inf, solution.best_time_to_buy_and_sell_stock([-math.inf, math.inf]))
        self.assertEqual(0, solution.best_time_to_buy_and_sell_stock([math.inf, -math.inf]))
        self.assertEqual(0, solution.best_time_to_buy_and_sell_stock([]))
        self.assertEqual(0, solution.best_time_to_buy_and_sell_stock([1]))
        self.assertEqual(3, solution.best_time_to_buy_and_sell_stock([-2, -1, 0, 1, -2]))

    def test_solution_zero_profit(self):
        self.assertEqual(0, solution.best_time_to_buy_and_sell_stock([2, 1]))
        self.assertEqual(0, solution.best_time_to_buy_and_sell_stock([3, 2, 1]))
        self.assertEqual(0, solution.best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]))

    def test_solution_positive_profit(self):
        self.assertEqual(2, solution.best_time_to_buy_and_sell_stock([1, 2, 3]))
        self.assertEqual(1, solution.best_time_to_buy_and_sell_stock([1, 2]))
        self.assertEqual(5, solution.best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))

    def test_solution_programmatically(self):
        random_high = random.randint(1000, 10000)
        random_low = random.randint(10, 20)
        expected_profit = random_high - random_low
        entries = []
        entries.append(random_low)
        for value in range(random_low + 1, random_high - 1):
            entries.append(value)
        entries.append(random_high)
        self.assertEqual(expected_profit, solution.best_time_to_buy_and_sell_stock(entries))


if __name__ == '__main__':
    unittest.main()
