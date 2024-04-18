from palindrome_number import is_number_palindrome
import pytest


@pytest.mark.parametrize("input_, expected_output", [
    (12321, True),
    (11112, False),
    (9876556789, True),
])
def test_is_number_palindrome(input_, expected_output):
    actual = is_number_palindrome(input_)
    assert actual == expected_output