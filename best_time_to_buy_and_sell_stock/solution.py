from typing import List


def best_time_to_buy_and_sell_stock(prices: List[int]) -> int:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    :param prices: a history of prices os shares
    :return: the max difference between low to high, when low index is prior the higher
    """
    # Check edge-cases
    if len(prices) <= 1:
        return 0

    # Check the rest of the scenarios
    highest = 0
    for start in range(0, len(prices) - 1):
        for end in range(start + 1, len(prices)):
            if (prices[end] - prices[start]) > highest:
                highest = prices[end] - prices[start]
    return highest
