from add_two_numbers import ListNode, add_two_numbers
import pytest


def test_case():
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))

    expected_output = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8)))

    assert add_two_numbers(l1, l2) == expected_output


pytest.main()