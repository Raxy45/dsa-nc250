class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        visited = set()
        def dfs(r, c):
            if min(r, c) == 0 or r==R-1 or c == C-1:
                # at boundary
                if board[r][c] == 'X': return True
                return False # 'O' present at boundary


            if (r, c) in visited:
                return True
            visited.add((r, c))
            res = dfs(r, c+1) and dfs(r+1, c) and dfs(r, c-1) and dfs(r-1, c)
            if res:
                board[r][c] = 'X'
            return res
        for r in range(len(board)):
            for c in range(len(board[r])):
                if min(r, c) == 0 or r==R-1 or c == C-1:
                    continue
                
                if board[r][c] == 'O' and (r, c) not in visited:
                    dfs(r, c)
        
    