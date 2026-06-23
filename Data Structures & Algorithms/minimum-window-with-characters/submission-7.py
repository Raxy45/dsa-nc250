class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed, formed = len(t), 0
        t_mp = Counter(t)

        s_mp = defaultdict(int)
        min_len = len(s)+1
        l = 0
        ans = ""
        for i in range(len(s)):
            s_mp[s[i]] += 1

            if s_mp[s[i]] == t_mp[s[i]]:
                formed += 1
            
            while l<=i and formed == needed:
                print('in here')
                if (i-l+1) < min_len:
                    ans = s[l:i+1]
                    min_len = min(i-l+1, min_len)
                s_mp[s[l]] -= 1
                if s_mp[s[l]] == 0:
                    del s_mp[s[l]]
                
                if s[l] in t_mp and s_mp[s[l]] < t_mp[s[l]]:
                    formed -= 1
                
                l+= 1
        return ans