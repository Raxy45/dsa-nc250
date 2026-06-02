class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(r, c, idx):
            if idx==len(word):
                return True
            
            # print(r, c, idx)
            if min(r, c)<0 or r==len(board) or c==len(board[0]) \
            or board[r][c] != word[idx] or (r, c) in visited:
                # print(r, c, visited)
                # print(word[idx], (r, c) in visited, idx)
                return False
            # print('searching', r, c, word[idx], board[r][c])
            
            visited.add((r, c))
            if dfs(r+1, c, idx+1) or dfs(r, c+1, idx+1) or \
            dfs(r-1, c, idx+1) or dfs(r, c-1, idx+1):
                return True
            visited.remove((r, c))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and dfs(i, j, 0):
                    return True
        return False
        