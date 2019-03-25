def length_longest_substring(full_string: str) -> int:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    :param full_string: string to analyze
    :return: length of the longest substring without repeating characters
    """
    string = full_string.lower()

    # Check edge-cases
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        return 1

    # Check the rest of the scenarios
    longest = 1
    for start in range(0, len(string) - 1):
        found = False
        for end in range(start + 1, len(string)):
            sub_string = string[start:end + 1]
            if not repeat_chars(sub_string) and len(sub_string) > longest:
                longest = len(sub_string)
                found = True
            elif found:
                break
    return longest


def repeat_chars(substring: str) -> bool:
    """
    :param substring: a string to analyze
    :return: True if has repeating characters False otherwise
    """
    string = substring.lower()
    for start in range(0, len(string)):
        for end in range(start + 1, len(string)):
            if string[start] == string[end]:
                return True
    return False
