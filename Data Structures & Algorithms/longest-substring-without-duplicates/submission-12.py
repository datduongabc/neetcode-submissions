class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        left, right, solution = 0, 0, 1
        char_set = set()

        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            solution = max(solution, right - left + 1)
            right += 1

        return solution