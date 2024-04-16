def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    total_len = len(nums1) + len(nums2)

    # index of the "merged" array
    merged_index_array = total_len / 2

    i = 0
    j = 0
    last_modified = None
    while i + j < merged_index_array:
        if i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
                last_modified = "i"
            else:
                j += 1
                last_modified = "j"
        elif i >= len(nums1):
            j += 1
            last_modified = "j"
        elif j >= len(nums2):
            i += 1
            last_modified = "i"

    if total_len % 2 == 0:
        if last_modified == "i":
            lower_number = nums1[i - 1]
        elif last_modified == "j":
            lower_number = nums2[j - 1]

        # get the next number
        if i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
                last_modified = "i"
            else:
                j += 1
                last_modified = "j"
        elif i >= len(nums1):
            j += 1
            last_modified = "j"
        elif j >= len(nums2):
            i += 1
            last_modified = "i"

        if last_modified == "i":
            higher_number = nums1[i - 1]
        elif last_modified == "j":
            higher_number = nums2[j - 1]
        return (lower_number + higher_number) / 2

    if last_modified == "i":
        return nums1[i - 1]
    if last_modified == "j":
        return nums2[j - 1]
    return nums2[j]