class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1. Find first letter in board
        # 2. If not found return False
        # 3. If found
        #     a. check right (r, c+1) of current -> matches proceed
        #     b. check bottom (r+1, c) of current -> matches proceed
        #     c. check left (r, c-1) of current ->  matches proceed
        #     d. check top (r-1, c) of current -> matches proceed

        def search(r, c, idx):
            if idx == len(word):
                return True
            if r == len(board) or c == len(board[0]) or board[r][c]!=word[idx]:
                return False
            
            # current_char matches first letter of word
            return search(r, c+1, idx+1) or search(r+1, c, idx+1) or \
                    search(r, c-1, idx+1) or search(r-1, c, idx+1) 
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if search(r, c, 0):
                        return True
        return False           

        
        