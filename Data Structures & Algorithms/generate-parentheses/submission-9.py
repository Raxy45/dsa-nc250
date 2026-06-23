class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(open, close):
            if (open+close) == n*2:
                ans.append("".join(subset))
                return
            
            if open<n:
                subset.append('(')
                open += 1
                solve(open, close)
                subset.pop()
                open -= 1

            if close<open:
                subset.append(')')
                close += 1
                solve(open, close)
                subset.pop()
                close -= 1
        
        ans, subset = [], []
        solve(0, 0)
        return ans