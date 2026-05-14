class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap, self.k = nums, k
        heapq.heapify(minHeap)

        while len(minHeap) > self.k:
            heapq.heappop(minHeap)

        return minHeap[0]