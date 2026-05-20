class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights)-1
        while l<r:
            c_len = r-l
            c_area = (c_len) * min(heights[l], heights[r])
            ans = max(ans, c_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans