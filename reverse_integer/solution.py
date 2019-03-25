def reverse(x: int) -> int:
    # Prepare value
    unsigned_value = (x // 10) if (x % 10 == 0) else x
    unsigned_value = -unsigned_value if x < 0 else unsigned_value

    # Do some maths
    new_value = 0
    while unsigned_value > 0:
        new_value = (new_value * 10) + (unsigned_value % 10)
        unsigned_value //= 10

    # Apply sign
    new_value = -new_value if x < 0 else new_value

    # Check boundaries
    if new_value < -(2 ** 31) or new_value >= (2 ** 31):
        return 0

    return new_value
