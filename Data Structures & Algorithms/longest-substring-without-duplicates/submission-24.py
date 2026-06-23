class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, i, j = 0, 0, 1
        w = set(s[0])
        while j<len(s):
            while j<len(s) and s[j] not in w:
                w.add(s[j])
                ans = max(ans, j-i)
                j += 1
            
            while j<len(s) and s[j] in w:
                w.remove(s[i])
                i += 1
        return ans + 1