from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        counter_s1 = Counter(s1)
        

        for i in range(len(s2) - window_size + 1):
            sub_s2 = s2[i:i+window_size]
            counter_sub_s2 = Counter(sub_s2)

            if counter_s1 == counter_sub_s2:
                return True

        return False