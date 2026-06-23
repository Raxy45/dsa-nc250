class Solution:
    def trap(self, height: List[int]) -> int:
        low, high = 0, len(height)-1
        l_max, r_max = 0, 0
        ans = 0

        while low<=high:
            if height[low]<height[high]:
                l_max = max(l_max,height[low])
                ans+= (l_max - height[low])
                low += 1
            else:
                r_max = max(r_max, height[high])
                ans += (r_max - height[high])
                high -= 1
        return ans