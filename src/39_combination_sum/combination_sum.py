from collections import defaultdict


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # sort the array so we can take shortcuts when we can
    candidates = sorted(candidates)

    cache = defaultdict(list)  # maps targets to the list of numbers that got those targets

    def inner_fn(target, candidates, path) -> list[list[int]]:

        # base cases
        if target == 0:
            return [path]

        if target == 1 or target < 0:
            # no solution
            return []  # the input is in range 2 < num < 40

        # recursive case
        # for each number in the array, make another call with that number and the new target
        non_null_paths = []
        for num in candidates:
            if target - num < 0 or target - num == 1:
                continue
            # to avoid duplicates, let's impose that smaller numbers can't ascend to big numbers
            if path and num < path[-1]:
                continue
            new_targ_results = inner_fn(target - num, candidates, path + [num])
            non_null_paths.extend(new_targ_results)

        return non_null_paths

    non_null_paths = inner_fn(target, candidates, path=[])

    return non_null_paths