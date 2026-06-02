class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(open, closed):
            if open+closed == 2*n:
                ans.append("".join(subset.copy()))
                return

            if open>closed:
                subset.append(')')
                dfs(open, closed+1)
                subset.pop()
            
            if open<n and open>=closed:
                subset.append('(')
                dfs(open+1, closed)
                subset.pop()

        ans, subset = [], []
        dfs(0,0)
        print(ans)
        return ans