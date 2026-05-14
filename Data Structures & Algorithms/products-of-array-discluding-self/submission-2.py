class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_1 = 1
        ans_2 = 1
        count = 0
        result = []

        for number in nums:
            if number == 0:
                ans_1 *= number
                count += 1

            # ans_1 0
            # ans_2 8
            # count 2
            else:
                ans_1 *= number
                ans_2 *= number

        if count > 1:
            return [0 for _ in range(len(nums))]

        for number in nums:
            if number == 0:
                result.append(ans_2)
            else:
                result.append(ans_1 // number)

        return result