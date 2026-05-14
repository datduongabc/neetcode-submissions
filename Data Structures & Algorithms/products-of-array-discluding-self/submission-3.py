class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        result = []

        for number in nums:
            if number == 0:
                count_zero += 1
            else:
                product *= number

        if count_zero > 1:
            return [0 for _ in range(len(nums))]

        for index, number in enumerate(nums):
            if count_zero == 0:
                result.append(product // number)
            else:
                if (number == 0):
                    result.append(product)
                else:
                    result.append(0)

        return result