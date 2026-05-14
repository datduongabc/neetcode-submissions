from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)

        for index, num in enumerate(nums):
            remain = target - num
            if remain not in hashMap:
                hashMap[num] = index
            else:
                return [hashMap[remain], index]