class Solution:

    def get_diff(self, t_arr, sub_arr):
        diff = 0
        for i in range(len(t_arr)):
            if (t_arr[i] - sub_arr[i])>0:
                diff += t_arr[i] - sub_arr[i]
        return diff

    def update_smp(self, l, r):
        s_hmp = [0]*52
        for i in range(r):
            s_hmp[ord(s[i])-ord('a')] += 1
        return s_hmp

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_hmp, window_hmp = {}, {}
        for i in range(len(t)):
            t_hmp[t[i]] = t_hmp.get(t[i], 0) + 1
        
        min_len = float('infinity')
        res_indices = [-1, -1]
        formed = 0
        l = 0
        required = len(t)

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
