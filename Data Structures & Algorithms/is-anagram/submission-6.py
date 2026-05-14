from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = defaultdict(int)

        for letter in s:
            hashMap[letter] += 1

        for letter in t:
            hashMap[letter] -= 1
            if hashMap[letter] == 0:
                del hashMap[letter]

        return len(hashMap) == 0