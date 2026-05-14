from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        solution = 0

        for num in nums:
            hashMap[num] += 1

        for num in nums:
            maxLength = 1
            nextValue = num + 1
            while nextValue in hashMap:
                maxLength += 1
                nextValue += 1
            
            solution = max(solution, maxLength)

        return solution