class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(used_open, used_closed, subset):
            if len(subset) == 2*n:
                ans.append("".join(subset))
                return
            
            if used_open<n:
                subset.append('(')
                solve(used_open+1, used_closed, subset)
                subset.pop()

            if used_closed < used_open and used_closed<n:
                subset.append(')')
                solve(used_open, used_closed+1, subset)
                subset.pop()
        
        ans = []
        solve(0,0, [])
        print(ans)
        return ans