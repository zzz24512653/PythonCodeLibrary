def bubble_sort(nums, reverse=False):
    """
    :param nums: nums is a list of numbers
    :param reverse: False means sort from small to big, otherwise is sort form big to small
    :return: nums after sorted
    """
    if nums is None or len(nums) < 2:
        return nums
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if reverse is True and nums[i] < nums[j] or reverse is False and nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
