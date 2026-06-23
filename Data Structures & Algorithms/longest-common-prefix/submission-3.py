class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if j == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans









        ans = ""
        for i in range(len(strs[0])):
            # print(i, strs[0][i])
            for j in range(1, len(strs)):
                # print(j, strs[j])
                if i>=len(strs[j]) or strs[0][i] != strs[j][i]:
                    return ans
            ans += strs[0][i]
            # print(ans)
            # print('8')
        return ans