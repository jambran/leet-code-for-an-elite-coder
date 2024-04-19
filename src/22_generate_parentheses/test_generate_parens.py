import pytest
from generate_parens import generate_parens


@pytest.mark.parametrize("n, expected", [
    (1, ["()"]),
    (2, ["()()", "(())"]),
    (3, ["()()()", "((()))", "()(())", "(())()", "(()())"]),
])
def test_generate_parens(n, expected):
    actual = generate_parens(n)

    assert set(actual) == set(expected)
