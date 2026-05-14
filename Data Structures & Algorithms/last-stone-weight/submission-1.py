class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-stone for stone in stones]
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            first = heapq.heappop(new_stones)
            second = heapq.heappop(new_stones)

            if second > first:
                heapq.heappush(new_stones, first - second)
            

        new_stones.append(0)
        return -new_stones[0]