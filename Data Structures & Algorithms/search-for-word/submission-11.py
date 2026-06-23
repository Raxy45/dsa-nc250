class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(visited, r, c, idx):
            print('in solve')
            if idx == len(word):
                print('reached end of word')
                return True
            if r==len(board) or c==len(board[r]) or (r,c) in visited or word[idx] != board[r][c]:
                # print(r, c, visited, word)
                return False
            
            print('here')
            visited.add((r, c))
            a = solve(visited, r, c+1, idx+1) or solve(visited, r+1, c, idx+1) or \
                solve(visited, r, c-1, idx+1) or solve(visited, r-1, c, idx+1)
            
            # print(a,'for idx', word[idx+1], r, c)
            visited.remove((r, c))
            return a
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]==word[0]:
                    print('calling')
                    if solve(set(), r, c, 0):
                        return True
        return False