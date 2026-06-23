class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        max_substr = 0
        for r in range(len(s)):
            while l<r and s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_substr = max(max_substr, len(window))
        return max_substr