class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        solution = [0] * size
        stack = []

        for index in reversed(range(size)):
            temp = temperatures[index]

            if index == size - 1:
                stack.append((index, temp))
                continue
            
            while len(stack) > 0 and temp >= stack[-1][1]:
                stack.pop()

            if len(stack) > 0:
                solution[index] = stack[-1][0] - index
            
            stack.append((index, temp))

        return solution