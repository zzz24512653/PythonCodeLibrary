def insert_sort(nums, reverse=False):
    if nums is None or len(nums) < 2:
        return nums
    for i in range(1, len(nums)):
        t = nums[i]
        j = i-1
        while j > -1:
            if reverse is True and nums[j] < t or reverse is False and nums[j] > t:
                nums[j+1] = nums[j]
            else:
                break
            j -= 1
        nums[j+1] = t
    return nums

