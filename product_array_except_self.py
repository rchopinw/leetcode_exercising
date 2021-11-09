# LC 238: Product of an array except self
def product_except_self(nums):
    prefix, suffix = [1], [1]
    for num1, num2 in zip(nums, nums[::-1]):
        prefix.append(prefix[-1] * num1)
        suffix.append(suffix[-1] * num2)
    suffix.reverse()
    return [x * y for x, y in zip(prefix, suffix[1:])]


def product_array_except_self_ii(nums):
    results = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        results[i] = results[i-1] * nums[i-1]
    sfx = 1
    for j in reversed(range(len(nums))):
        results[j] *= sfx
        sfx *= nums[j]
    return results
