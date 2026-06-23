class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(c_sum, i):
            if c_sum == target:
                ans.append(subset.copy())
                return
            
            if c_sum > target or i==len(nums):
                return
            
            subset.append(nums[i])
            dfs(c_sum+nums[i], i)

            subset.pop()
            dfs(c_sum, i+1)
        
        ans, subset = [], []
        dfs(0, 0)
        return ans