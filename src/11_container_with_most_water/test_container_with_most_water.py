import pytest

from container_with_most_water import container_with_most_water


@pytest.mark.parametrize("arr, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
])
def test_container_with_most_water(arr, expected):
    actual = container_with_most_water(arr)
    assert actual == expected
