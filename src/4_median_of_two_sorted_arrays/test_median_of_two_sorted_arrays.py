import pytest
from median_of_two_sorted_arrays import find_median_sorted_arrays

@pytest.mark.parametrize("nums1,nums2,expected", [
    ([1, 3], [2], 2),
    ([1, 2, 3, 4], [5, 5, 5], 4),
])
def test_case(nums1, nums2, expected):
    result = find_median_sorted_arrays(nums1, nums2)

    assert result == expected


pytest.main()
