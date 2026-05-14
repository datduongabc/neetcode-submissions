class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = set()
        
        for index, num in enumerate(nums):
            # 1 số cố định và 2 con trỏ cho 2 số còn lại
            left, right = index + 1, len(nums) - 1

            while left < right:
                if num + nums[left] + nums[right] < 0:
                    left += 1
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    solution.add((num, nums[left] , nums[right]))
                    left += 1
                    right -= 1
        
        return [list(res) for res in solution]