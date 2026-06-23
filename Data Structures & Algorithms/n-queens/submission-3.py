class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        queens_to_be_placed = n
        temp = board
        # ans = []
        # for r in temp:
        #     ans.append(",".join(r))
        # print(ans)
        used_column = [False] * n
        final_ans = []

        def diag_check(current_row, current_col, used_queen_pos):
            for used_row, used_col in used_queen_pos:
                if abs(current_row - used_row) == abs(current_col - used_col):
                    return False
            return True
        def solve(r):
            if r == n:
                # reached a valid combo return this
                ans = []
                for x in board:
                    ans.append("".join(x))
                final_ans.append(ans)
                return

            for c in range(0, n):
                if not used_column[c] and (r-c) not in diag1 and (r+c) not in diag2:
                    board[r][c] = 'Q'
                    used_column[c] = True
                    diag1.add(r-c)
                    diag2.add(r+c)

                    solve(r+1)

                    board[r][c] = '.'
                    used_column[c] = False
                    diag1.remove(r-c)
                    diag2.remove(r+c)

        diag1, diag2 = set(), set()
        solve(0)
        return final_ans