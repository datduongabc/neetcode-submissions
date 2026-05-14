class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasAppear = dict()
        
        for index, num in enumerate(nums):
            remaining_value = target - num

            if remaining_value not in hasAppear:
                hasAppear[num] = index
            else:
                first_index = index
                second_indedx = hasAppear[remaining_value]
                return [min(first_index, second_indedx), max(first_index, second_indedx)]