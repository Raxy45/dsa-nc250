class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        l, r = 0, len(heights)-1
        while l<r:
            width = r-l
            if heights[l] < heights[r]:
                max_w = max(max_w, width*heights[l])
                l += 1
            else:
                max_w = max(max_w, width*heights[r])
                r -= 1
        return max_w