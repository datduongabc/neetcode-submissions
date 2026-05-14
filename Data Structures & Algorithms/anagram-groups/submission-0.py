class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            LIST = [0] * 26
            for letter in word:
                LIST[ord(letter) - ord('a')] += 1
            
            TUPLE = tuple(LIST)
            result[TUPLE].append(word)

        return list(result.values())