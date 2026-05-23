class Solution:
    def trap(self, height: List[int]) -> int:
        ans, l_mx, r_mx = 0, 0, 0
        l, r = 0, len(height) - 1
        while l<r:
            if height[l]<height[r]:
                l_mx = max(l_mx, height[l])
                ans += (l_mx - height[l])
                l += 1
            else:
                r_mx = max(r_mx, height[r])
                ans += (r_mx - height[r])
                r -= 1
        return ans









        ans, l_max, r_max = 0, 0, 0
        l, r = 0, len(height)-1
        while l<r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)
            print(l, l_max, r, r_max, ans)
            if l_max < r_max:
                ans += l_max - height[l]
                l += 1
            else:
                ans += r_max - height[r]
                r -= 1
            print(l, l_max, r, r_max, ans)
        return ans