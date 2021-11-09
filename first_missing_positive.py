# LC 41: First missing positive
def first_missing_positive(nums):
    if 1 not in nums:
        return 1
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = 1
    for i in range(len(nums)):
        a = abs(nums[i])
        if a == len(nums):
            nums[0] = -abs(nums[0])
        else:
            nums[a] = -abs(nums[a])
    for i in range(1, len(nums)):
        if nums[i] > 0:
            return i
    if nums[0] > 0:
        return len(nums)
    return len(nums) + 1


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)