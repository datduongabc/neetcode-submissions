class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) < 2):
            return False
    
        stack = []
        
        for letter in s:
            if letter == '[' or letter == '(' or letter == '{':
                stack.append(letter)
            elif letter == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif letter == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif letter == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0