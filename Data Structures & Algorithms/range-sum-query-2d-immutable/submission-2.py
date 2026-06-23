class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.r, self.c = len(matrix), len(matrix[0])
        print(self.r, self.c)
        self.sumM = [[0 for k in range(self.c+1)] for i in range(self.r+1)]
        
        for i in range(self.r):
            current_row_sum = 0
            for j in range(self.c):
                current_row_sum += matrix[i][j]
                upper_sum = self.sumM[i][j+1]
                self.sumM[i+1][j+1]=current_row_sum+upper_sum
        print(self.sumM)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = self.sumM[row2+1][col2+1]
        diag = self.sumM[row1][col1]
        top_right = self.sumM[row1][col2+1]
        bottom_left = self.sumM[row2+1][col1]

        return total_sum-top_right-bottom_left+diag


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)