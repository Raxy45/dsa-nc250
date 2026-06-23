class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []

        def solve(idx):
            if idx==len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[idx])
            solve(idx+1)

            subset.pop()
            solve(idx+1)
        
        solve(0)
        return ans