def length_of_longest_substring(s: str) -> int:
    # what if we create a map of character to last index we saw this character at?
    # when we iterate to the next character, if the character exists in the map,
    # then we know the difference

    character_to_index = {}
    start_index = 0
    candidate_length = 0
    for i, char in enumerate(s, start=1):
        start_index = max(
            character_to_index.get(char, 0),
            start_index,
        )

        this_substring_length = i - start_index

        if this_substring_length > candidate_length:
            candidate_length = this_substring_length

        character_to_index[char] = i

    return candidate_length
