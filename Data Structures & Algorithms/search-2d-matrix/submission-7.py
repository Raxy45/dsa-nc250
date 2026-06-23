class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)
        C = len(matrix[0]) - 1
        while L <= R:
            M = (L+R)//2
            if matrix[M][0] <= target <= matrix[M][C]:
                break
            
            if target < matrix[M][0]:
                R = M - 1
            else:
                L = M + 1
        
        l, r = 0, C
        while l<=r:
            m = (l+r)//2
            if matrix[M][m] == target:
                return True
            
            if matrix[M][m] < target:
                l = m + 1
            else:
                r = m -1
        return False