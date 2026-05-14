class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for word in strs:
            LIST = [0] * 26
            for letter in word:
                LIST[ord(letter) - ord('a')] += 1

            TUPLE = tuple(LIST)
            output[TUPLE].append(word)

        return list(output.values())