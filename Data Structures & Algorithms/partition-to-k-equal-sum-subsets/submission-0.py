class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        each_K_th_sum = sum(nums)//k
        if k%1 > 0:
            return False
        
        sides = [0] * k
        def dfs(i):
            if i == len(nums):
                return True

            for side in range(k):
                if (nums[i] + sides[side]) <= each_K_th_sum:
                    sides[side] += nums[i]
                    if dfs(i+1):
                        return True
                    sides[side] -= nums[i]
            return False
        
        return dfs(0)
