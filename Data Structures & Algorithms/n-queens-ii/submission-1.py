class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]
        queens_to_be_placed = n
        temp = board
        used_column = [False] * n
        final_ans = 0

        def solve(r):
            if r == n:
                # reached a valid combo return this
                final_ans += 1
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