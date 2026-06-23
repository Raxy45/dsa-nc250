class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        R, C = len(board), len(board[0])
        visited = set()
        def dfs(r, c):
            if min(r, c) < 0 or r==R or c==C or board[r][c]=='X':
                return

            board[r][c] = 'T'
            visited.add((r, c))
            dfs(r, c+1)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r-1, c)

        for r in range(R):
            if board[r][0] == 'O':
                dfs(r, 0)
            
            if board[r][C-1] == 'O':
                dfs(r, C-1)

        for c in range(C):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[R-1][c] == 'O':
                dfs(R-1, c)
        

        for r in range(R):
            for c in range(C):
                if board[r][c] != 'T':
                    board[r][c] = 'X'
                
                if board[r][c] == 'T':
                    board[r][c] = 'O'
 