class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_mp = defaultdict(int)
        max_str = 0
        ans = 0
        j = 0
        for i in range(len(s)):
            char_mp[s[i]] += 1
            max_str = max(max_str, char_mp[s[i]])
            while j<i and (max_str - len(char_mp)) > k:
                char_mp[s[j]] -= 1
                if char_mp[s[j]] == 0:
                    del char_mp[s[j]] 
                max_str = max(max_str, char_mp[s[j]])
                j += 1
            ans = max(ans, i-j)
        return ans+1
