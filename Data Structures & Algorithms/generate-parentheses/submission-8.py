class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, subset = [], []
        used_open, used_closed = 0, 0

        def solve(subset, used_open, used_closed):
            if used_open == used_closed == n:
                ans.append("".join(subset.copy()))
                return
            
            if used_open < n:
                subset.append('(')
                used_open += 1
                solve(subset, used_open, used_closed)

                subset.pop()
                used_open -= 1

            if used_closed < used_open:
                subset.append(')')
                used_closed += 1
                solve(subset, used_open, used_closed)

                subset.pop()
                used_closed -= 1
            
        solve([], used_open, used_closed)
        return ans