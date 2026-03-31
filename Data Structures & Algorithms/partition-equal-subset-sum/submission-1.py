class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)%2) > 0: return False
        t = sum(nums)//2
        def solve(t, idx):
            if t==0:
                return True
            
            for i in range(idx, len(nums)):
                if t>=nums[i] and solve(t-nums[i], i+1):
                    return True
            return False
        return solve(t, 0)