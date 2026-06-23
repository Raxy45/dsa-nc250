class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        l, min_w = 0, len(nums)+1
        for r in range(len(nums)):
            curr_sum += nums[r]
            while l<r and curr_sum >= target:
                curr_sum -= nums[l]
                min_w = min(r-l+1, min_w)
                l += 1
        if min_w < len(nums)+1: return min_w
        return 0