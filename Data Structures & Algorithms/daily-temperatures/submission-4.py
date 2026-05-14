class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Method 1
        # ans = [0] * len(temperatures)
        # stack = [] # [index, temperature]

        # for index, temperature in enumerate(temperatures):
        #     while stack and temperature > stack[-1][1]:
        #         stackIndex, stackTem = stack.pop()
        #         ans[stackIndex] = index - stackIndex

        #     stack.append([index, temperature])

        # return ans

        # Method 2
        size = len(temperatures)
        ans = [0] * size
        stack = []

        for i in range(size - 2, -1, -1):
            j = i + 1
            while j < size and temperatures[j] <= temperatures[i]:
                if ans[j] == 0:
                    j = size
                    break

                j += ans[j]

            if j < size:
                ans[i] = j - i

        return ans