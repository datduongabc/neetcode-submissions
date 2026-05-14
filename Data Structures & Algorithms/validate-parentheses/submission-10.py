class Solution:
    def isValid(self, s: str) -> bool:
        if s.startswith(')') or s.startswith(']') or s.startswith('}'):
            return False
        
        if s.endswith('(') or s.endswith('[') or s.endswith('{'):
            return False

        stack = []

        for paren in s:
            if paren == '(' or paren == '[' or paren == '{':
                stack.append(paren)
            else:
                if stack:
                    if (paren == ')' and stack[-1] == '(') or (paren == ']' and stack[-1] == '[') or (paren == '}' and stack[-1] == '{'):
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0