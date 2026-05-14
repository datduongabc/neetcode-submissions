class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # [index, temperature]

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stackIndex, stackTem = stack.pop()
                ans[stackIndex] = index - stackIndex

            stack.append([index, temperature])

        return ans