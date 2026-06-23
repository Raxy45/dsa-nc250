class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        t_hmp, s_hmp = {}, {}
        for i in range(len(t)):
            t_hmp[t[i]] = t_hmp.get(t[i], 0) + 1
        
        l=0
        res = [-1,-1]
        formed = 0
        needed = len(t_hmp)
        min_string = len(s)+1
        for r in range(len(s)):
            s_hmp[s[r]] = s_hmp.get(s[r], 0)+1
            if s[r] in t and s_hmp[s[r]]==t_hmp[s[r]]:
                formed += 1
            
            while formed==needed:
                if (r-l+1)<min_string:
                    min_string = r-l+1
                    res = [l,r]

                s_hmp[s[l]]-=1
                if s[l] in t and s_hmp[s[l]]<t_hmp[s[l]]:
                    formed -= 1
                l += 1

        l, r = res
        if min_string==len(s)+1:
            return ""
        return s[l:r+1]
        if t == "":
            return ""

        t_hmp, window_hmp = {}, {}
        for i in range(len(t)):
            t_hmp[t[i]] = t_hmp.get(t[i], 0) + 1
        
        min_len = float('infinity')
        res_indices = [-1, -1]
        formed = 0
        l = 0
        required = len(t_hmp)

        for r in range(len(s)):
            current_char = s[r]
            window_hmp[current_char] = window_hmp.get(current_char, 0) + 1
            if current_char in t and window_hmp[current_char] == t_hmp[current_char]:
                formed += 1

            while formed == required:
                if (r-l+1) < min_len:
                    res_indices = [l, r]
                    min_len = r - l + 1
                current_char = s[l]
                window_hmp[current_char] -= 1
                if current_char in t and window_hmp[current_char] < t_hmp[current_char]:
                    formed -= 1
                l += 1
        l, r = res_indices
        if min_len == float("infinity"):
            return ""
        return s[l:r+1]

                
        # Brute
        min_sub = s
        for i in range(0, len(s)-1):
            current_str = s[i]
            for j in range(i+1, len(s)):
                current_str = s[i:j+1]
                if len(set(t)) <= len(set(current_str)):
                    if len(current_str) < len(min_sub):
                        min_sub = current_str
        return min_sub

        # if len(t) > len(s):
        #     return ""
        
        # l = 0
        # r = len(t)
        # ans = s[l:r]
        # min_ss = len(s)
        # while r<len(s):
