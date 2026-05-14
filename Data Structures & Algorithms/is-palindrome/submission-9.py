import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left <= right:
            leftWord, rightWord = s[left], s[right]
            if re.match(r"[^a-zA-Z0-9]", leftWord):
                left += 1
            elif re.match(r"[^a-zA-Z0-9]", rightWord):
                right -= 1
            else:
                if leftWord.lower() != rightWord.lower():
                    return False
                else:
                    left += 1
                    right -= 1

        return True