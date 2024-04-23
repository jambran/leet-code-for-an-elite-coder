from combination_sum import combination_sum
import pytest


@pytest.mark.parametrize(
    "candidates,target,expected", [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3], 5, [[2, 3]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ]
)
def test_combination_sum(candidates, target, expected):
    actual = combination_sum(candidates, target)
    assert actual == expected
