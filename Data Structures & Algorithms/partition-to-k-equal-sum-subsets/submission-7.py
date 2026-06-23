class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum%k > 0: return False
        if max(nums) > (total_sum/k): return False

        required_sum = total_sum/k
        a = [0] * k
        nums.sort(reverse=True)

        def solve(idx):
            if idx == len(nums):
                return True
            
            for i in range(k):
                if (a[i] + nums[idx]) <= required_sum:
                    a[i] += nums[idx]
                    if solve(idx+1):
                        return True
                    a[i] -= nums[idx]
            
                if a[i] == 0:
                    break
            return False
        return solve(0)