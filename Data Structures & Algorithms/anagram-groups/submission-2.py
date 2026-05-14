from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            wordMap = [0] * 26
            for letter in word:
                wordMap[ord(letter) - ord('a')] += 1
            hashMap[tuple(wordMap)].append(word) # Vì key ko được là list nên chuyển sang tuple

        return list(hashMap.values())