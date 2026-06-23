class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        temp = []

        used = {
            'row':set(),
            'cols':set(),
            'diag1':set(),
            'diag2':set()
        }
        board = []
        for i in range(n):
            temp = []
            for k in range(n):
                temp.append('.')
            board.append(temp)

        # board = [['.'] for i in range(n)] for k in range(n):
        # print(board)
        def solve(r):
            # print('used', used)
            if r == n:
                print('ans')
                print(used)
                print(board)
                curr_ans = []
                for row in board:
                    curr_ans.append("".join(row))
                ans.append(curr_ans)
                # ans.append(board.copy())
                return

            for c in range(n):
                if r in used['row'] or c in used['cols'] \
                or r+c in used['diag1'] or r-c in used['diag2']:
                    continue
                
                used['row'].add(r)
                used['cols'].add(c)
                used['diag1'].add(r+c)
                used['diag2'].add(r-c)
                board[r][c] = 'Q'

                solve(r+1)
                
                used['row'].remove(r)
                used['cols'].remove(c)
                used['diag1'].remove(r+c)
                used['diag2'].remove(r-c)
                board[r][c] = '.'
        solve(0)
        return ans