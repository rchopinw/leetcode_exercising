import heapq


# LC: kth largest element in an array
def find_kth_largest(nums, k):
    pq =[]
    for num in nums:
        if len(pq) >= k:
            if pq and num > pq[0]:
                heapq.heappushpop(pq, num)
        else:
            heapq.heappush(pq, num)
    return pq[0]


class KthLargest:

    def __init__(self, k: int, nums):
        self.pq = []
        self.k = k
        self._initialize_heap(nums)

    def add(self, val: int) -> int:
        if len(self.pq) == self.k:
            if self.pq[0] < val:
                heapq.heappushpop(self.pq, val)
        else:
            heapq.heappush(self.pq, val)
        return self.pq[0]

    def _initialize_heap(self, nums):
        for num in nums:
            if len(self.pq) == self.k:
                if self.pq[0] < num:
                    heapq.heappushpop(self.pq, num)
            else:
                heapq.heappush(self.pq, num)