class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, c_sum):
            nonlocal final_sum
            if i == len(nums):
                final_sum += c_sum
                return
        
            dfs(i+1, c_sum)

            c_sum = c_sum ^ nums[i]
            dfs(i+1, c_sum)
        
        final_sum = 0
        dfs(0,0)
        return final_sum