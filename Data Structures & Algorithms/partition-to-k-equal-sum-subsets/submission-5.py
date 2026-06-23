class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def solve(idx, remaining_k, curr):
            if remaining_k == 0: return True

            for j in range(idx, len(nums)):
                if used[j]:
                    continue
                
                if (curr+nums[j]) > target:
                    break
                
                used[j] = True
                if (curr+nums[j] == target):
                    return solve(j+1, remaining_k-1, 0)
                
                used[j] = True
                curr += nums[j]
                if solve(j+1, remaining_k, curr):
                    return True
                
                used[j] = False
                curr -= nums[j]
            return False
        return solve(0, k, 0)