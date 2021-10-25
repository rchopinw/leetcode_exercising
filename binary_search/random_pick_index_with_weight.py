# LC 528 Random Pick With Weight
from random import random


class RandomPickWeight:
    def __init__(self, w):
        self.w_prefix = self._cal_prefix(w)
        self.norm = self.w_prefix[-1]

    def pick_index(self, ):
        return self._binary_search(random() * self.norm)

    def _binary_search(self, v):
        left, right = 0, len(self.w_prefix)
        while left < right:
            mid = left + (right - left) // 2
            if self.w_prefix[mid] < v:
                left = mid + 1
            else:
                right = mid
        return left

    def _cal_prefix(self, nums):
        s = 0
        prefix = []
        for num in nums:
            s += num
            prefix.append(s)
        return prefix
