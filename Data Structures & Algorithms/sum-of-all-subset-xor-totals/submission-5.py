class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def dfs(idx, curr_sum):
            nonlocal ans
            if idx==len(nums):
                ans += curr_sum 
                return
            
            dfs(idx+1, curr_sum^nums[idx])
            dfs(idx+1, curr_sum)
        dfs(0, 0)
        return ans