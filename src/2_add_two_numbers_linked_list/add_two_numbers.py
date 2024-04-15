from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={repr(self.next)})"

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    first = l1
    second = l2

    result_start = None
    result_curr = None
    need_to_carry_the_1 = False
    while first or second or need_to_carry_the_1:
        first_val = first.val if first else 0
        second_val = second.val if second else 0
        val = first_val + second_val

        if need_to_carry_the_1:
            val += 1
        new_node = ListNode(
            val=val % 10,
        )
        need_to_carry_the_1 = val >= 10
        if result_curr is None:
            result_curr = new_node
            result_start = new_node
        else:
            result_curr.next = new_node
            result_curr = result_curr.next

        first = first.next if first else None
        second = second.next if second else None

    return result_start