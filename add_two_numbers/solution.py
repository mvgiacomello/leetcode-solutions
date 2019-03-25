from typing import List


def add_two_numbers(list1: List, list2: List) -> List:
    # Requirement is that numbers should be positive
    if list1[-1] < 0 or list2[-1] < 0 or len(list1) == 0 or len(list2) == 0:
        raise ValueError('numbers should be positive and non empty')

    result = []
    list1_index = 0
    list2_index = 0
    carry = 0
    while (list1_index < len(list1)) or (list2_index < len(list2)) or (carry > 0):
        # Get the value of each
        l1_val = 0 if list1_index >= len(list1) else list1[list1_index]
        l2_val = 0 if list2_index >= len(list2) else list2[list2_index]

        # Do some math
        current_sum = carry + l1_val + l2_val
        carry = current_sum // 10
        current_value = current_sum % 10

        # Store result
        result.append(current_value)

        # Go to next
        list1_index += 1
        list2_index += 1
    return result[::-1]
