class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h_mp = defaultdict(int)
        ans, max_f, i = 0, 0, 0
        for j in range(len(s)):
            h_mp[s[j]] += 1
            max_f = max(max_f, h_mp[s[j]])
            # print(h_mp)
            # print(j-i+1, max_f, j, j, i)
            while ((j-i+1) - max_f) > k:
                # print('here', i, j)
                h_mp[s[i]] -= 1
                if h_mp[s[i]] == 0: del h_mp[s[i]]
                i += 1
            ans = max(ans, j-i+1)
        return ans