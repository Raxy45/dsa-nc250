class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        i = 0
        for j in range(len(s)):
            while i<j and s[j] in seen:
                seen.remove(s[i])
                i += 1
            ans = max(ans, j-i+1)
            seen.add(s[j])
        return ans
        