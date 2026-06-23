class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def solve(idx, curr):
            nonlocal total
            if idx == len(nums):
                total += curr
                return
            
            include = curr ^ nums[idx]
            exclude = curr
            solve(idx+1, include)
            solve(idx+1, exclude)

        solve(0,0)
        return total