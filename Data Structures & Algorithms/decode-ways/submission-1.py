class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        def solve(start, indx):
            nonlocal ans
            # print(start, indx)
            if indx == len(s) and start!=len(s):
                ans += 1
                return
            
            # print(s[start:indx+1])
            # print(s[start:indx+1])
            if start==len(s) or int(s[start:indx+1]) == 0 or int(s[start:indx+1])>26:
                return
            
            solve(start, indx+1)
            solve(indx+1, indx+1)
        
        solve(0, 0)
        return ans