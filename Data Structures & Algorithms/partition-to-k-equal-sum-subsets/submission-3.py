class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        each_K_th_sum = sum(nums)//k
        if sum(nums)%k != 0:
            return False
        
        sides = [0] * k
        nums.sort(reverse=True)
        print(nums)
        print(each_K_th_sum)
        def dfs(i):
            if i == len(nums):
                return True

            for side in range(k):
                if (nums[i] + sides[side]) <= each_K_th_sum:
                    sides[side] += nums[i]
                    if dfs(i+1):
                        return True
                    sides[side] -= nums[i]
                
                if sides[side] == 0:
                    break
            return False
        
        return dfs(0)
