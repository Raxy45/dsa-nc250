class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def solve(idx, total):
            if idx==len(nums):
                return total
            
            include = total ^ nums[idx]
            exclude = total

            return solve(idx+1, include) + solve(idx+1, exclude)
        
        return solve(0,0)