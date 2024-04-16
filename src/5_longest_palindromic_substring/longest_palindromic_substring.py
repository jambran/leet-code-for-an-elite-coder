import math


def determine_palindrome_from_midpoint(s: str, midpoint_index: float) -> str:
    # we found the middle point. Return the candidate string that goes along with it
    i = math.floor(midpoint_index - .5)
    j = math.ceil(midpoint_index + .5)

    if int(midpoint_index) == midpoint_index:
        result = [s[midpoint_index]]
    else:
        result = []

    while 0 <= i and j < len(s) and s[i] == s[j]:
        result.insert(0, s[i])
        result.append(s[j])
        i -= 1
        j += 1
    return "".join(result), i + 1, j - 1


def longest_palindrome(s: str) -> str:
    # use a stack to determine palindromes
    if s == "":
        return ""

    palindrome_middle_indices = []

    for i, char in enumerate(s):
        letter_before = s[i - 1] if 0 < i <= len(s) else None
        two_letters_before = s[i - 2] if 0 <= i - 2 <= len(s) else None
        if char == two_letters_before:
            palindrome_middle_indices.append(i - 1)
        if char == letter_before:
            palindrome_middle_indices.append(i - .5)

    candidate_palindrome = ""

    if not palindrome_middle_indices:
        return "" if not s else s[0]

    for middle_index in palindrome_middle_indices:
        palindrome_from_this_point, start_index, end_index = determine_palindrome_from_midpoint(s, middle_index)

        if len(palindrome_from_this_point) > len(candidate_palindrome):
            candidate_palindrome = palindrome_from_this_point

    if candidate_palindrome == "":
        candidate_palindrome = s[0]
    return candidate_palindrome
