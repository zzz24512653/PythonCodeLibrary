def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


def sift_up(nums, i, comp):
    # assert nums[1:i] is a heap
    while i != 1:
        if comp(nums[i], nums[i/2]):
            swap(nums, i, i / 2)
            i /= 2
        else:
            break


def sift_down(nums, i, comp):
    # assert heap[1:i] is a heap
    j = 1
    while j*2 < i:
        t = j*2
        if t+1 < i and comp(nums[t+1], nums[t]):
            t += 1
        if comp(nums[t], nums[j]):
            swap(nums, j, t)
            j = t
        else:
            break


def heap_sort(nums, reverse=False):
    if nums is None or len(nums) < 2:
        return nums
    # build heap
    heap = [" "]
    heap.extend(nums)
    for i in range(2, len(heap)):
        if reverse is True:
            sift_up(heap, i, lambda a, b: a < b)  # build minimal heap
        else:
            sift_up(heap, i, lambda a, b: a > b)  # build maximal heap
    # sort
    for i in range(len(heap)-1, 1, -1):
        swap(heap, 1, i)
        # rebuild heap
        if reverse is True:
            sift_down(heap, i, lambda a, b: a < b)  # select smaller
        else:
            sift_down(heap, i, lambda a, b: a > b)  # select bigger
    return heap[1:]
