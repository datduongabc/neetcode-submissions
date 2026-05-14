class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)

        maxLength = 0

        for num in new_set:
            if num - 1 not in new_set:
                current = num
                freq = 1
                while current + 1 in new_set:
                    current += 1
                    freq += 1

                maxLength = max(maxLength, freq)

        return maxLength