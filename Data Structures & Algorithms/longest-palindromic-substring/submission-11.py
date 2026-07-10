class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_pali(l, r):
            print(l, r)
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        ans, curr_pali_odd, curr_pali_even = "", "", ""
        n = len(s)
        for i in range(n):
            print('get_pali called for', i)
            curr_pali_odd = get_pali(i-1, i+1)
            if len(curr_pali_odd) > len(ans):
                ans = curr_pali_odd

            if i>0 and s[i] == s[i-1]:
                curr_pali_even = get_pali(i-2, i+1)
            if len(curr_pali_even) > len(ans):
                ans = curr_pali_even
            

        return ans
