from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k: int) -> int:
            sum = 0
            for pile in piles:
                sum += ceil(pile / k)
            return sum

        left, right = 1, max(piles)

        while left <= right:
            middle = left + (right - left) // 2
            
            if helper(middle) > h:
                left = middle + 1
            elif helper(middle) <= h:
                right = middle - 1

        return left