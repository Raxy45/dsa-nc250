class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rh = 0, len(matrix)-1
        col = len(matrix[0])-1
        while rl<=rh:
            mid = (rl+rh)//2
            if matrix[mid][0]<= target <=matrix[mid][col]:
                break
            
            if target < matrix[mid][0]: rh = mid - 1
            else: rl = mid + 1
        
        if rl > rh:
            return False

        low, high = 0, col
        while low<=high:
            mid_c = (low+high)//2
            if matrix[mid][mid_c] == target:
                return True
            
            if matrix[mid][mid_c] > target:
                high = mid_c - 1
            else:
                low = mid_c + 1
        return False
