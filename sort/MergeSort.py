def merge_two(nums1, nums2, comp):
    merged_nums = []
    while len(nums1) != 0 and len(nums2) != 0:
        if comp(nums1[0], nums2[0]):
            merged_nums.append(nums1.pop(0))
        else:
            merged_nums.append(nums2.pop(0))
    if len(nums1) != 0:
        merged_nums.extend(nums1)
    if len(nums2) != 0:
        merged_nums.extend(nums2)
    return merged_nums


def merge_sort(nums, reverse=False):
    """
    :param nums: nums is a list of numbers
    :param reverse: False means sort from small to big, otherwise is sort form big to small
    :return: nums after sorted
    """
    if nums is None or len(nums) < 2:
        return nums
    nums_l = merge_sort(nums[:len(nums)/2], reverse)
    nums_r = merge_sort(nums[len(nums)/2:], reverse)
    if reverse is True:
        return merge_two(nums_l, nums_r, lambda a, b: a > b)
    else:
        return merge_two(nums_l, nums_r, lambda a, b: a < b)

