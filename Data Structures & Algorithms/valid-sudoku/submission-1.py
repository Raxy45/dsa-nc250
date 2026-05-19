class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rd, cd, dd = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                # row 
                if board[i][j] == '.': continue
                if board[i][j] in rd[i] or board[i][j] in cd[j]:
                    return False
                
                rd[i].add(board[i][j])
                cd[j].add(board[i][j])

                msr, msc = i//3, j//3
                if board[i][j] in dd[(msr, msc)]:
                    return False
                dd[(msr, msc)].add(board[i][j])
        return True