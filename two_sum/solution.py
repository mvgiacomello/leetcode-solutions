from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    https://leetcode.com/problems/two-sum/
    :param nums: list of integers
    :param target: expected sum
    :return: list of two index of the two integers that when summed are equals to target
    :raises: ValueError when combination not found or input list has only 1 element
    """
    if len(nums) < 2:
        raise ValueError('nums argument should have more than 1 value')
    hash_table = {}
    for index, value in enumerate(nums):
        lookup = target - value
        if lookup in hash_table:
            return [hash_table[lookup], index]
        else:
            hash_table[value] = index
    raise ValueError('no sum of two values were found to reach the target')
