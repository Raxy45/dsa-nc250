class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row, cols, left_bottom, left_top = set(), set(), set(), set()

        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        def dfs(r):
            if r==n:
                curr_ans = []
                for ur in range(n):
                    curr_ans.append("".join(board[ur]))
                ans.append(curr_ans)
                return
            
            for j in range(n):
                if r in row or j in cols:
                    continue
                    
                if (r-j) in left_bottom or (j+r) in left_top:
                    continue
                    
                queen_added = True
                row.add(r)
                cols.add(j)
                left_bottom.add(r-j)
                left_top.add(r+j)
                board[r][j] = 'Q'
                dfs(r+1)

                board[r][j] = '.'
                row.remove(r)
                cols.remove(j)
                left_bottom.remove(r-j)
                left_top.remove(r+j)
            return False
        dfs(0)
        # print(ans)
        return ans
