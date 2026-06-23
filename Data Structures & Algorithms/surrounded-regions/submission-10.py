class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        visited = set()

        def solve(r, c):
            # print('visiting',r,c)
            if min(r,c)<0 or r==R or c==C: 
                return False
            
            if board[r][c] == 'X': return True
            if (r, c) in visited: return True

            
            visited.add((r, c))
            final = solve(r, c+1) and solve(r+1, c) and solve(r, c-1) and solve(r-1, c)
            if final:
                board[r][c]='X'
            return final
        for r in range(R):
            for c in range(C):
                if board[r][c]=='O' and (r,c) not in visited:
                    solve(r, c)