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
                # print('word matched')
                return True
            if (r == len(board) or r<0) or (c == len(board[0]) or c<0) or board[r][c]!=word[idx] or board[r][c]=='#':
                # print('char at board[r][c]', board[r][c], 'did not matched', word[idx])
                return False
            

            # seen.add((r, c))
            print('current r, c, idx', r, c, idx)
            print('formed elems')
            # print('current char in board', board[r][c])
            print('elem at idx', word[idx])
            print('*'*4)
            temp = board[r][c]
            board[r][c] = '#'
            # current_char matches first letter of word
            found = (search(r, c+1, idx+1) or search(r+1, c, idx+1) or \
                    search(r, c-1, idx+1) or search(r-1, c, idx+1))
            # seen.remove((r,c))
            board[r][c] = temp
            return found
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    # seen = set()
                    if search(r, c, 0):
                        return True
        return False           

        
        