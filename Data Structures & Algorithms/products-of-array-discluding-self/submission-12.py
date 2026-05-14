class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = [1]
        right_left = [1]
        size = len(nums)

        idx = 1
        product = 1
        while idx < size:
            product *= nums[idx - 1]
            left_right.append(product)
            idx += 1

        idx = size - 2
        product = 1
        while idx >= 0:
            product *= nums[idx + 1]
            right_left.append(product)
            idx -= 1
        
        for idx in range(size):
            left_right[idx] = left_right[idx] * right_left[size - 1 - idx]

        return left_right