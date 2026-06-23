class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.sumM = [[0]*(COL+1) for _ in range(ROW+1)]

        for r in range(ROW):
            prefix_sum = 0
            for c in range(COL):
                prefix_sum += matrix[r][c]
                above_summation = self.sumM[r][c+1]
                self.sumM[r+1][c+1] = prefix_sum + above_summation

                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1+1,col1+1,row2+1,col2+1
        above = self.sumM[r1-1][c2]
        left =self.sumM[r2][c1-1]
        diaginal = self.sumM[r1-1][c1-1]
        return self.sumM[r2][c2] - above - left + diaginal


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)