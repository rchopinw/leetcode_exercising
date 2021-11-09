# LC 528 Random Pick With Weight
from random import random


class RandomPickWeight:
    def __init__(self, w):
        self.w_prefix = self.__cal_prefix(w)
        self.norm = self.w_prefix[-1]

    def pick_index(self, ):
        return self.__binary_search(random() * self.norm)

    def __binary_search(self, v):
        left, right = 0, len(self.w_prefix) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.w_prefix[mid] < v:
                left = mid + 1
            else:
                right = mid
        return left

    def __cal_prefix(self, nums):
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])
        return prefix[1:]
