class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if (total_sum % k) > 0:
            return False

        nums.sort(reverse=True)
        required_each_subset_sum = total_sum / k
        sides = [0] * k
        def solve(idx):
            if idx==len(nums):
                return True

            for i in range(k):
                if (sides[i] + nums[idx]) <= required_each_subset_sum:
                    sides[i] += nums[idx]
                    if solve(idx+1):
                        return True

                    sides[i] -= nums[idx]
                
                if sides[i] == 0:
                    break
            return False

        return solve(0)