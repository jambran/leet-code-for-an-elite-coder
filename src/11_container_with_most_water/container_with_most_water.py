

def container_with_most_water(arr: list[int]) -> int:
    i = 0
    j = len(arr) - 1

    max_area = 0
    while i < j:
        area = min(arr[i], arr[j]) * (j - i)
        max_area = max(area, max_area)
        if arr[i] <= arr[j]:
            i += 1
        else:
            j -= 1

    return max_area