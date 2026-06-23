class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        current_row = row1
        sum_ans = 0
        while(current_row<=row2):
            current_column = col1
            while(current_column<=col2):
                sum_ans += self.matrix[current_row][current_column]
                current_column += 1
            current_row += 1
        return sum_ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)