def length_longest_substring(full_string: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    :param full_string: string to analyze
    :return: length of the longest substring without repeating characters
    """
    string = full_string.lower()
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        return 1
    else:
        # TODO: implement me
        return -1
