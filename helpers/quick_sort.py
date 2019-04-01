from typing import List


class Sort:

    def recursive_quick_sort(self, list: List[int]) -> List[int]:
        '''
        :param list: to be sorted
        :return: sorted copy of the list
        '''
        if len(list) > 900:
            raise RecursionError('Due to python stack size, you cannot sort more than 900 elements.'
                                 'Recursion would not finish.')
        if len(list) == 1:
            return [list[0]]
        elif len(list) == 0:
            return []
        else:
            # Put all the elements lower than list[0] to the left and greater to the right, recursively
            left = self.recursive_quick_sort([value for value in list[1:] if value < list[0]])
            right = self.recursive_quick_sort([value for value in list[1:] if value >= list[0]])
            return left + [list[0]] + right
