def bubble_sort(nums, reverse=False):
    """
    :param nums: nums is a list of numbers
    :param reverse: False means sort from small to big, otherwise is sort form big to small
    :return: nums after sorted
    """
    if nums is None or len(nums) < 2:
        return nums
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if reverse is True and nums[j] < nums[j+1] or reverse is False and nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


