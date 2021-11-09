# LC 42 trapping the rain water
def trap_monotonic_stack(heights):
    stack, ans = [], 0
    for i in range(len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            low = heights[stack.pop()]
            if not stack:
                break
            ans += (min(heights[stack[-1]], heights[i]) - low) * (i - stack[-1] - 1)
    return ans


def trap_two_pointers(heights):
    """
    Space complexity: O(1) constant space complexity
    :param heights:
    :return:
    """
    ans = 0
    left_max, right_max = 0, 0
    left, right = 0, len(heights) - 1
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] < left_max:
                ans += left_max - heights[left]
            else:
                left_max = heights[left]
            left += 1
        else:
            if heights[right] < right_max:
                ans += right_max - heights[right]
            else:
                right_max = heights[right]
            right -= 1
    return ans
