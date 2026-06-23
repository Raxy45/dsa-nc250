class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        mini_squares = defaultdict(set) # key is (row//3, col//3)

        for r in range(9):
            for c in range(9):
                c_e = board[r][c]
                if c_e == '.':
                    continue
                
                if c_e in rows[r] or c_e in cols[c]:
                    return False
                
                mini_square_row = r//3
                mini_square_col = c//3
                if c_e in mini_squares[(mini_square_row, mini_square_col)]:
                    return False
                
                rows[r].add(c_e)
                cols[c].add(c_e)
                mini_squares[(mini_square_row, mini_square_col)].add(c_e)
        return True