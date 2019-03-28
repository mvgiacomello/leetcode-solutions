def is_valid(s: str) -> bool:
    stack = []
    for index in range(len(s)):
        if s[index] in '({[':
            stack.append(s[index])
        elif len(stack) == 0:
            return False
        else:
            top = stack.pop()
            if (top == '{' and s[index] != '}') or (top == '[' and s[index] != ']') or (top == '(' and s[index] != ')'):
                return False
    return len(stack) == 0
