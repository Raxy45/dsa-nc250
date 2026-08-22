class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * (n) for _ in range(n+1)]
        for i in range(n):
            dp[1][i] = True
            # one char lengths
        
        ans = s[0]
        for curr_len in range(2, n+1):
            for i in range(n-curr_len+1):
                j = i + curr_len - 1
                if curr_len==2:
                    if s[i] == s[j]:
                        dp[curr_len][i] = dp[curr_len][j] = True
                        ans = s[i:j+1]
                        continue
                if s[i] == s[j] and dp[curr_len-2][i+1] and dp[curr_len-2][j-1]:
                    dp[curr_len][i] = dp[curr_len][j] = True
                    ans = s[i: j+1]
        return ans























        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        n = len(s)
        ans = ""
        for l in range(1, n+1):
            for i in range(0, n+1-l):
                j = i + l - 1
                if l==1:
                    dp[i][j] = True
                elif l==2 and s[i] == s[j]:
                    dp[i][j] = True
                    
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] and l > len(ans):
                    ans = s[i:j+1]
        return ans
                

    def longestPalindromeBasic(self, s: str) -> str:
        def get_pali(l, r):
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        ans, curr_pali_odd, curr_pali_even = "", "", ""
        n = len(s)
        for i in range(n):
            curr_pali_odd = get_pali(i-1, i+1)
            if len(curr_pali_odd) > len(ans):
                ans = curr_pali_odd

            if i>0 and s[i] == s[i-1]:
                curr_pali_even = get_pali(i-2, i+1)
            if len(curr_pali_even) > len(ans):
                ans = curr_pali_even
            

        return ans
