class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total%2) > 0: return False
        req_sum = total//2
        dp = set()
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = nums[i]
            for j in range(i+1, len(nums)):
                curr_sum += nums[j]
                if curr_sum == req_sum: return True
        return False