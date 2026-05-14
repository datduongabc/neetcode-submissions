class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sList = [0] * 26
        tList = [0] * 26

        for index in range (0, len(s)):
            sList[ord(s[index]) - ord('a')] += 1
            tList[ord(t[index]) - ord('a')] += 1

        if sList == tList:
            return True

        return False