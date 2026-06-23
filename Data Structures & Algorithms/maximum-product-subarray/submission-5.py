class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        min_v, max_v = 1, 1
        for n in nums:
            max_v = max(n, min_v*n, max_v*n)
            min_v = min(n, min_v*n, max_v*n)
            ans = max(ans, min_v, max_v)
        return ans