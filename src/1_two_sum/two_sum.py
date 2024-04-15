from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # one pass
    number_to_index = {}
    for i, num in enumerate(nums):

        candidate = target - num
        if candidate in number_to_index:
            if number_to_index[candidate] != i:
                return number_to_index[candidate], i

        number_to_index[num] = i

    return -1, -1


if __name__ == '__main__':
    nums_and_targets = [
        ([2, 7, 11, 15], 9, (0, 1)),
    ]
    for nums, target, expected_output in nums_and_targets:
        print(f"{nums} with target {target} -> {two_sum(nums, target)}. Expected {expected_output}")
