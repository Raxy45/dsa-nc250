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
        def solve(r, used, used_queen_poss):
            if r == n:
                # reached a valid combo return this
                ans = []
                for x in board:
                    ans.append("".join(x))
                # print('current r, c', r, c)
                print('adding ans', ans, 'to final ans')
                final_ans.append(ans)
                return

            for c in range(0, n):
                if not used[c] and diag_check(r, c, used_queen_poss):
                    board[r][c] = 'Q'
                    used[c] = True
                    used_queen_poss.append((r, c))

                    solve(r+1, used, used_queen_poss)

                    board[r][c] = '.'
                    used[c] = False
                    used_queen_poss.pop()

        solve(0, used_column, [])
        return final_ans