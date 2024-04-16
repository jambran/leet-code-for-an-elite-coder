from longest_substring_without_repeating_characters import length_of_longest_substring
import pytest


def test_case():
    s = "abcabcbb"
    expected = 3
    actual = length_of_longest_substring(s)
    assert actual == expected


pytest.main()
