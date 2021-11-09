# LC 398: Random Pick Index
from random import choice
from collections import deque, defaultdict


class Solution:
    def __init__(self, nums):
        self.rec = self._arange(nums)

    def pick(self, target: int) -> int:
        return choice(self.rec[target])

    def _arange(self, nums):
        record = defaultdict(list)
        for i, num in enumerate(nums):
            record[num].append(i)
        return record