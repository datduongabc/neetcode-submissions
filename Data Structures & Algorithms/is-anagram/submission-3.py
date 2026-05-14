class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = dict()

        for _ in s:
            sDict[_] = sDict.get(_, 0) + 1
        
        for _ in t:
            if _ not in sDict:
                return False
            else:
                sDict[_] = sDict.get(_, 0) - 1

        for _, freq in sDict.items():
            if freq != 0:
                return False

        return True   