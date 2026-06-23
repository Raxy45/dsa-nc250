class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque([])
        for r in range(len(board)):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][-1] == 'O':
                q.append((r, len(board[0]-1)))
        
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                q.append((0, c))
            
            if board[-1][c] == 'O':
                q.append((len(board)-1, c))

        visited = set()
        print(q)
        while q:
            r, c = q.popleft()
            print('popped', r, c)
            if (r, c) in visited: continue
            if min(r, c) < 0 or r==len(board) or c==len(board[0]): continue
            if board[r][c] == 'X': continue
            board[r][c] = 'I'
            visited.add((r, c))
            q.append((r, c+1))
            q.append((r, c-1))
            q.append((r+1, c))
            q.append((r-1, c))
        
        print(board)
        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if board[r][c] == 'O':
                    # print(bo)
                    board[r][c] = 'X'
                elif board[r][c] == 'I':
                    board[r][c] = 'O'
        # print
                
        
