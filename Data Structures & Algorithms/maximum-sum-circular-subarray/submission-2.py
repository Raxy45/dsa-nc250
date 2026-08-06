class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curr = 0
        for n in nums:
            curr = max(curr+n, n)
            maxSum = max(maxSum, curr)
        # print(maxSum)
        minSum = float('inf')
        curr = 0
        for n in nums:
            curr = min(curr+n, n)
            minSum = min(minSum, curr)
        
        total_sum = sum(nums)
        if total_sum == minSum:
            return maxSum
        
        return max(maxSum, total_sum-minSum)
