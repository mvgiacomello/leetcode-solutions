def is_valid(input: str) -> bool:
    """
    https://leetcode.com/problems/valid-parentheses/
    :param input: a string with {, (, [, ], ) and }
    :return: True if a list represent a correct order
    """
    stack = []
    for index in range(len(input)):
        if input[index] in '({[':
            stack.append(input[index])
        elif len(stack) == 0:
            return False
        else:
            top = stack.pop()
            if ((top == '{' and input[index] != '}') or
                    (top == '[' and input[index] != ']') or
                    (top == '(' and input[index] != ')')):
                return False
    return len(stack) == 0
