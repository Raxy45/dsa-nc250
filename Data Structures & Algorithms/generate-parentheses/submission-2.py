class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(used_open, used_closed, subset):
            print('current str', subset)
            print('used (, used )', used_open, used_closed)
            if used_closed > used_open or used_open>n or used_closed>n:
                return

            if len(subset) == 2*n:
                ans.append(subset)
                return
            
            if used_open<n:
                subset+='('
                solve(used_open+1, used_closed, subset)
                subset = subset[:len(subset)-1]

            if used_closed < used_open and used_closed<n:
                subset+=')'
                solve(used_open, used_closed+1, subset)
        
        ans = []
        solve(0,0, '')
        print(ans)
        return ans