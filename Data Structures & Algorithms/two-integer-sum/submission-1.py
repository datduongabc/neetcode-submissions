class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasAppear = dict()
        
        for index in range (len(nums)):
            remaining_value = target - nums[index]

            if remaining_value not in hasAppear:
                hasAppear[nums[index]] = index
            else:
                first_index = index
                second_indedx = hasAppear[remaining_value]
                return [min(first_index, second_indedx), max(first_index, second_indedx)]