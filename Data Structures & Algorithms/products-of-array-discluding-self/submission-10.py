class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = [1]
        right_left = [1]

        idx = 1
        product = 1
        while idx < len(nums):
            product *= nums[idx - 1]
            left_right.append(product)
            idx += 1

        idx = len(nums) - 2
        product = 1
        while idx >= 0:
            product *= nums[idx + 1]
            right_left.append(product)
            idx -= 1
        
        for i in range(len(left_right)):
            left_right[i] = left_right[i] * right_left[len(left_right) - 1 - i]

        return left_right