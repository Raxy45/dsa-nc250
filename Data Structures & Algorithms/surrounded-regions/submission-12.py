class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        visited = set()

        temp = [[True for _ in range(C)] for _ in range(R)]
        print(temp)
        def solve(r, c):
            if min(r, c)<0 or r==R or c==C or board[r][c]=='X' or (r, c) in visited:
                return

            temp[r][c]=False
            visited.add((r, c))
            solve(r, c+1)
            solve(r+1, c)
            solve(r, c-1)
            solve(r-1, c)

        for r in range(R):
            if board[r][0] == 'O':
                solve(r, 0)
            
            if board[r][C-1] == 'O':
                solve(r, C-1)
        
        for c in range(C):
            if board[0][c] == 'O':
                solve(0, c)
            
            if board[R-1][c] == 'O':
                solve(R-1, c)

        for r in range(0, R):
            for c in range(0, C):
                if r>0 and c>0 and r<R-1 and c<C-1:
                    if temp[r][c]:
                        board[r][c]="X"
