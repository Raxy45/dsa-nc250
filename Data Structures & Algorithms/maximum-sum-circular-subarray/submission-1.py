class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax
        
class SolutionME:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mx_sum, min_sum = nums[0], nums[0]
        c_sum = nums[0]
        for i in range(1, len(nums)):
            c_sum = max(nums[i], c_sum + nums[i])
            mx_sum = max(c_sum, mx_sum)

        c_sum = nums[0]
        for i in range(1, len(nums)):
            c_sum = min(nums[i], c_sum + nums[i])
            min_sum = min(min_sum, c_sum)

        if mx_sum>0: return max(mx_sum, sum(nums)-min_sum)
        return mx_sum
    


