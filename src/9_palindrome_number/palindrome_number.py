import math
def is_number_palindrome(n: int) -> bool:
    """
    let's do this without casting to a string
    """
    digits = []
    while n > 0:
        final_digit = n % 10
        digits.append(final_digit)

        n = math.floor(n / 10)

    for i in range(math.ceil(len(digits) / 2)):
        if digits[i] != digits[len(digits) - 1 - i]:
            return False

    return True
