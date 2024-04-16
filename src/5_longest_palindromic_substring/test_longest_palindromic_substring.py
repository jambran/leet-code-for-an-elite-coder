import pytest
from longest_palindromic_substring import longest_palindrome


@pytest.mark.parametrize("input,output", [
    ("babad", "bab"),
])
def test_longest_palindromic_substring(input, output):
    actual = longest_palindrome(input)
    assert actual == output
