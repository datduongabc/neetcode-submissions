class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasAppear = dict()
        newList = []
        
        for index in range (len(nums)):
            remaining_value = target - nums[index]

            if remaining_value not in hasAppear:
                hasAppear[nums[index]] = index
            else:
                newList.append(index)
                newList.append(hasAppear[remaining_value])

                newList.sort()

        return newList