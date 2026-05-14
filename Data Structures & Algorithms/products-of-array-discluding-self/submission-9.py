class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left_right = [1]
        # right_left = [1]

        # idx = 1
        # product = 1
        # while idx < len(nums):
        #     product *= nums[idx - 1]
        #     left_right.append(product)
        #     idx += 1

        # idx = len(nums) - 2
        # product = 1
        # while idx > 0:
        #     product *= nums[idx + 1]
        #     left_right.append(product)
        #     idx -= 1
        
        # for i in range(len(left_right)):
        #     left_right[i] = left_right[i] * right_left[len(left_right) - 1 - i]

        # return left_right

        left_right = []
        right_left = []

        left_right.append(1)
        for i in range(1, len(nums), 1):
            left_right.append(1 * left_right[i - 1] * nums[i - 1])

        right_left.append(1)
        for i in range(1, len(nums), 1):
            right_left.append(1 * right_left[i - 1] * nums[len(nums) - i])

        right_left = right_left[::-1]

        res = []
        for i in range(len(left_right)):
            res.append(left_right[i] * right_left[i])

        return res