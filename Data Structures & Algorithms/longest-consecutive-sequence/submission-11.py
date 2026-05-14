class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
            
        new_set = set(nums)
        freq = 1
        maxLength = 1

        for num in new_set:
            if num - 1 not in new_set:
                current = num
                while current + 1 in new_set:
                    current += 1
                    freq += 1

                maxLength = max(maxLength, freq)
                freq = 1

        return maxLength