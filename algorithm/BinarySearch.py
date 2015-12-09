def binary_search(nums, l, r, t):
    if nums is None or len(nums) == 0:
        return None
    if l > r:
        return -1
    m = l + (r - l) / 2
    if nums[m] == t:
        return m
    elif nums[m] > t:
        return binary_search(nums, 0, m - 1, t)
    else:
        return binary_search(nums, m + 1, r, t)


if __name__ == "__main__":
    test_cases = [[], [1], [-1, 0, 1]]
    targets = [-10, -1, 0, 1, 20]
    for test_case in test_cases:
        for target in targets:
            print test_case, target, binary_search(test_case, 0, len(test_case)-1, target)
