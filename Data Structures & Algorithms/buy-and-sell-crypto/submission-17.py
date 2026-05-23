class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min_pr = nums[0]
        ans = 0
        for i in range(1, len(nums)):
            min_pr = min(min_pr, nums[i])
            ans = max(ans, nums[i] - min_pr)
        return ans