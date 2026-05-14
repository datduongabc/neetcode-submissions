class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:                
            if char in "+-*/":
                if len(stack) >= 2:
                        value_2 = stack.pop()
                        value_1 = stack.pop()

                        if char == "+":
                            stack.append(value_1 + value_2)
                        elif char == "-":
                            stack.append(value_1 - value_2)
                        elif char == "*":
                            stack.append(value_1 * value_2)
                        else:
                            if value_2 == 0:
                                raise ZeroDivisionError("divide by zero")
                            else:
                                stack.append(int(value_1 / value_2))
            else:
                stack.append(int(char))
        
        return stack[-1]