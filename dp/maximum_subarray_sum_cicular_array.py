# LC 918 Maximum sum cicular array
def maximum_subarray(nums):
    low, high, optimal_low, optimal_high, s = [nums[0]] * 5
    for num in nums[1:]:
        low = min(num, low + num)
        high = max(num, high + num)
        optimal_low = min(optimal_low, low)
        optimal_high = max(optimal_high, high)
        s += num
    return max(s - optimal_low, optimal_high) if s != optimal_low else optimal_high
