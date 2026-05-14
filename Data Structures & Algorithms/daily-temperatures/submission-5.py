class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0] * len(temperatures)
        stack = []

        for index in reversed(range(len(temperatures))):
            temp = temperatures[index]

            if index == len(temperatures) - 1:
                stack.append((index, temp))
                continue
            
            while len(stack) > 0 and temp >= stack[-1][1]:
                stack.pop()

            if len(stack) > 0:
                solution[index] = stack[-1][0] - index
            
            stack.append((index, temp))

        return solution