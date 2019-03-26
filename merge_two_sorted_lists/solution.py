from helpers.linked_list import LinkedListNode


def merge_two_lists(list1: LinkedListNode, list2: LinkedListNode):
    """
    https://leetcode.com/problems/merge-two-sorted-lists/
    :param list1: sorted linked list
    :param list2: sorted linked list
    :return: combined sorted linked list
    """
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1
    else:
        if list1.value < list2.value:
            list1.next = merge_two_lists(list1.next, list2)
            return list1
        else:
            list2.next = merge_two_lists(list1, list2.next)
            return list2
