from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_counter = defaultdict(int)
        left = solution = 0
        
        for right in range(len(s)):
            s_counter[s[right]] += 1
            max_value = max(s_counter.values())
            window_size = right - left + 1
            if window_size - max_value <= k:
                solution = max(solution, window_size)
            else:
                s_counter[s[left]] -= 1
                left += 1
        return solution