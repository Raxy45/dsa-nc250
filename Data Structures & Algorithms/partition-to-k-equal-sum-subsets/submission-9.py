class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum%k > 0: return False

        req = total_sum/k
        groups = [0] * k

        def dfs(idx):
            if idx==len(nums):
                return True
            
            for i in range(k):
                if (nums[idx] + groups[i]) <= req:
                    groups[i] += nums[idx]

                    if dfs(idx+1): return True

                    groups[i] -= nums[idx]
                if groups[i] == 0: break
            return False
        return dfs(0)
        