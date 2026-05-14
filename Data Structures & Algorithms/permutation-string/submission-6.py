from collections import defaultdict, Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = defaultdict(int)
        left = 0

        for right in range(0, len(s2)):
            s2_counter[s2[right]] += 1
            if right - left + 1 == len(s1):
                if s2_counter != s1_counter:
                    s2_counter[s2[left]] -= 1

                    if s2_counter[s2[left]] == 0:
                        del s2_counter[s2[left]]
                    
                    left += 1
                else:
                    return True

        return False