from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    https://leetcode.com/problems/3sum/
    Considering this solution is O(n^3), it's not a good one.
    Might need to do some magic with hashmap that I still need to think about.
    :param nums: list of values to analyze
    :return: list of unique values that the sum is zero
    """

    # Edge-case handling
    if len(nums) < 3:
        return []

    # Rest of scenarios
    result = {}
    nums.sort()
    for a in range(0, len(nums) - 2):
        for b in range(a + 1, len(nums) - 1):
            for c in range(b + 1, len(nums)):
                if (nums[a] + nums[b] + nums[c] != 0):
                    continue  # Just to avoid having to evaluate next line
                elif (nums[a], nums[b], nums[c]) not in result:
                    result[(nums[a], nums[b], nums[c])] = [nums[a], nums[b], nums[c]]
    print('Result: ' + str(list(result.values())))
    return list(result.values())
