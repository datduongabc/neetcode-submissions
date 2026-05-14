class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Left = 0
        Right = len(numbers) - 1

        while Left < Right:
            if (numbers[Left] + numbers[Right] > target):
                Right -= 1
            elif (numbers[Left] + numbers[Right] < target):
                Left += 1
            else:
                return [Left + 1, Right + 1]

        return []

