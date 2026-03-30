class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        min_v = max_v = 1
        for n in nums:
            print(n)
            print('till now', ans, min_v, max_v)
            updated_mx = max(n, min_v*n, max_v*n)
            updated_min = min(n, min_v*n, max_v*n)
            ans = max(ans, updated_min, updated_mx)
            min_v, max_v = updated_min, updated_mx
            print('after', ans, min_v, max_v)
            print('****')
        return ans