class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        for i in range(0, len(height)-1):
            for j in range(i+1, len(height)):
                current_height = min(height[i], height[j])
                current_length = j - i
                current_area = current_height * current_length
                # print('c_h, c_l ', current_height, current_length)
                area = max(area, current_area)
        return area
        
        