from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        
        maxHeap = []
        for key, value in hashMap.items():
            heapq.heappush(maxHeap, (-value, key))

        solution = []
        while k > 0:
            value, key = heapq.heappop(maxHeap)
            solution.append(key)
            k -= 1

        return solution