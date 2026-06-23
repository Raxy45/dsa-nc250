class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        l_mx, r_mx = height[l], height[r]

        w = 0
        while l<r:
            l_mx, r_mx = max(height[l], l_mx), max(height[r], r_mx)

            if l_mx<r_mx:
                w += (l_mx - height[l])
                l += 1
            else:
                w += (r_mx - height[r])
                r -= 1
        return w