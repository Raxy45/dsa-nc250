class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.R, self.C = len(matrix), len(matrix[0])
        self.sumM = [[0 for i in range(self.C+1)] for _ in range(self.R+1)]

        for i in range(self.R):
            curr_sum = 0
            for j in range(self.C):
                curr_sum += matrix[i][j]
                self.sumM[i+1][j+1] = curr_sum + self.sumM[i][j+1]
        
        print(self.sumM)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        u_r = self.sumM[row1][col2+1]
        b_l = self.sumM[row2+1][col1]
        diag = self.sumM[row2+1][col2+1]
        b_diag = self.sumM[row1][col1]
        return diag - u_r - b_l + b_diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)