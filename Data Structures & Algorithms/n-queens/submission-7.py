class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [(['.'] * n) for _ in range(n)]
        
        visited = {'c': set(), 'diag1': set(), 'diag2': set()}

        def solve(row):
            if row == n:
                # print('finally got a match')
                # print(board)
                temp_board = []
                for r in range(n):
                    curr_row = "".join(board[r])
                    temp_board.append(curr_row)
                ans.append(temp_board)
                # print(ans)
                return
            
            if row>n: return

            for i in range(n):
                if i in visited['c'] or (row-i) in visited['diag1'] or (row+i) in visited['diag2']:
                    # print(row, i, visited['c'], visited['diag1'], visited['diag2'])
                    # print('continue')
                    continue
                
                # print('adding Q to', row, i)
                visited['c'].add(i)
                visited['diag1'].add(row-i)
                visited['diag2'].add(row+i)
                board[row][i] = 'Q'
                solve(row+1)
                
                # print('Removing Q stored at', row, i)
                board[row][i] = '.'
                visited['c'].remove(i)
                visited['diag1'].remove(row-i)
                visited['diag2'].remove(row+i)
            # print('no output')
        ans = []
        solve(0)
        print(ans)
        return ans
