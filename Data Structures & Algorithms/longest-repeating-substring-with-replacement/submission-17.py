class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_mp= defaultdict(int)
        i, ans, max_f = 0, 0, 0
        for j in range(len(s)):
            char_mp[s[j]] += 1
            max_f = max(max_f, char_mp[s[j]])
            
            while ((j - i + 1) - max_f) > k:
                char_mp[s[i]] -= 1
                if char_mp[s[i]] == 0: 
                    del char_mp[s[i]]
                i += 1
            
            ans = max(ans, j - i + 1)
        return ans