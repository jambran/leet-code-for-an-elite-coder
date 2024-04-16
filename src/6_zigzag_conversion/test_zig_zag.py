from zig_zag import convert

import pytest


@pytest.mark.parametrize("input,num_rows,expected", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
])
def test_zig_zag(input, num_rows, expected):
    actual = convert(input, num_rows)
    assert actual == expected
