class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_mp = Counter(t)
        needed, formed = len(t_mp), 0

        # needed is assigned to dict, because:
        # 1. We consider formed +=1 when the frequency of current char is exactly equal to the char in 2
        s_mp = defaultdict(int)
        min_len = len(s)+1
        l = 0
        ans = ""
        for i in range(len(s)):
            s_mp[s[i]] += 1

            if s_mp[s[i]] == t_mp[s[i]]:
                # When char frequencies exactly match up
                formed += 1
            
            print(formed)
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
            
        if ans == "" and formed==needed:
            return s[l:i+1]
        return ans