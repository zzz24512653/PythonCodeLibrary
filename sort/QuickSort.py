def partition(nums, l, r, comp):
    if l > r:
        return
    i = l  # i is the final position of nums[l]
    for j in range(l+1, r+1):
        if comp(nums[j], nums[l]):
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[l], nums[i] = nums[i], nums[l]
    partition(nums, l, i-1, comp)
    partition(nums, i+1, r, comp)


def quick_sort(nums, reverse=False):
    """
    :param nums: nums is a list of numbers
    :param reverse: False means sort from small to big, otherwise is sort form big to small
    :return: nums after sorted
    """
    if nums is None or len(nums) == 0:
        return nums
    if reverse is True:
        partition(nums, 0, len(nums)-1, lambda a, b: a > b)
    else:
        partition(nums, 0, len(nums)-1, lambda a, b: a < b)
    return nums

