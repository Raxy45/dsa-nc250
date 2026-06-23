class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        j, max_l, window = 0, 0, set()
        for i in range(len(s)):
            while j<=i and s[i] in window:
                window.remove(s[j])
                max_l = max(max_l, i - j)
                j += 1

            window.add(s[i])
        return max(max_l, len(window))