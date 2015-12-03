def shell_insert(nums, step, comp):
    for i in range(len(nums)):
        t = nums[i]
        j = i - step
        while j > -1:
            if comp(nums[j], t):
                nums[j+step] = nums[j]
            else:
                break
            j -= step
        nums[j+step] = t


def shell_sort(nums, reverse=False):
    if nums is None or len(nums) < 2:
        return nums
    steps = [5, 3, 1]
    for step in steps:
        if reverse is True:
            shell_insert(nums, step, lambda a, b: a < b)
        else:
            shell_insert(nums, step, lambda a, b: a > b)
    return nums
