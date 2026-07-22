class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            for next_str in strs[1:]:
                if i == len(next_str) or strs[0][i]!= next_str[i]: return ans
            ans += strs[0][i]
        return ans
        