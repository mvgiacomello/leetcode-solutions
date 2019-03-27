from helpers.linked_list import LinkedListNode


def reverse_list(head: LinkedListNode):
    """
    https://leetcode.com/problems/reverse-linked-list
    :param head: the first entry of a linked list
    :return: first node of the same linked list in reverse
    """
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        previous = None
        current = head
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
