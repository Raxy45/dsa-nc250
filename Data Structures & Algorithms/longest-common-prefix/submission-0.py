class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                    return pref
            pref += s[i]
        return pref
        