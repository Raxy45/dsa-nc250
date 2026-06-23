class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height)-1
        while l < r:
            current_width = r - l
            c_area = min(height[l], height[r]) * current_width

            area = max(c_area, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area
    def maxAreaBasic(self, height: List[int]) -> int:
        area = 0
        for i in range(0, len(height)-1):
            for j in range(i+1, len(height)):
                current_height = min(height[i], height[j])
                current_length = j - i
                current_area = current_height * current_length
                # print('c_h, c_l ', current_height, current_length)
                area = max(area, current_area)
        return area

        