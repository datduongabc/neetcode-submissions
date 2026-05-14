class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left <= right:
            leftValue, rightValue = numbers[left], numbers[right]
            if leftValue + rightValue > target:
                right -= 1
            elif leftValue + rightValue < target:
                left += 1
            else:
                return [left + 1, right + 1]