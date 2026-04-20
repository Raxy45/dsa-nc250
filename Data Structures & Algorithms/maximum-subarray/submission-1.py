class Solution:
    def maxSubArray(self, nums):
        res, curr_sum = float('-inf'), 0
        for num in nums:
            curr_sum = max(num, curr_sum+num)
            res = max(res, curr_sum)
        return res
class SolutionKadane:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr_sum= float('-inf'), 0
        for num in nums:
            curr_sum += num
            res = max(res, curr_sum)
            if curr_sum<0:
                curr_sum = 0
        return res
        
class SolutionNSquare:
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                res = max(res, cur)
        return res
    