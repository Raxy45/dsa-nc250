class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, h = 0, r-1
        mid = -1
        while l<=h:
            mid = (l+h)//2
            if target<matrix[mid][0]:
                h = mid - 1
            elif target > matrix[mid][c-1]:
                l = mid+1
            else:
                break
            
        row = mid
        l, h = 0, c-1
        while l<=h:
            mid = (l+h)//2
            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False
        