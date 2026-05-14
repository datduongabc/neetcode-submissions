from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = defaultdict(int) # Có thể sài set để tối ưu bộ nhớ hơn
        solution = 0

        for num in nums:
            hashMap[num] += 1

        for num in nums:
            if num - 1 not in hashMap: # Sự khác biệt giữa On và On^2 là ở dòng này
                maxLength = 1
                nextValue = num + 1
                while nextValue in hashMap:
                    maxLength += 1
                    nextValue += 1
                
                solution = max(solution, maxLength)

        return solution