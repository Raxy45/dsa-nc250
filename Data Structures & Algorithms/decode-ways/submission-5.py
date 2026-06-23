class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        def solve(i):
            nonlocal ans
            print(i)
            if i==len(s):
                ans += 1 
                return
            
            if int(s[i])<=0: return 
            solve(i+1)

            if (i+1)<len(s) and int(s[i:i+2])<27:
                print('called from', i)
                solve(i+2)
            print('here for', i)
        solve(0)
        return ans