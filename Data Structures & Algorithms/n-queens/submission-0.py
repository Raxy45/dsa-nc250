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

        def solve(queens_to_be_placed, r, c, used):
            if r == n and queens_to_be_placed == 0:
                # reached a valid combo return this
                ans = []
                for x in board:
                    ans.append(",".join(x))
                print('current r, c', r, c)
                print('adding ans', ans, 'to final ans')
                final_ans.append(ans)
                return True

            if r == n and queens_to_be_placed > 0:
                # reached the end and queens unplaced -> return False
                return False

            for c_r in range(r, n):
                for c_c in range(0, n):
                    if used[c_c]:
                        # column is used 
                        continue
                    
                    #if  how to check if the current position has element in its diagonal?
                        # continue

                    board[c_r][c_c] = 'Q'
                    used[c_c] = True
                    print('going for c', c_c)
                    solve(queens_to_be_placed - 1, c_r+1, c, used)
                    board[c_r][c_c] = '.'
                    used[c_c] = False
            
            return board

        solve(n, 0, 0, used_column)
        return final_ans