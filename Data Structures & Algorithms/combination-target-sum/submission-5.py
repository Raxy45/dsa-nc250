class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, res = [], []

        def solve(idx, total):
            if total == target:
                ans.append(res.copy())
                return
            
            if idx==len(nums) or total>target:
                return
            
            res.append(nums[idx])
            solve(idx, total+nums[idx])
            res.pop()

            solve(idx+1, total)
        
        solve(0, 0)
        return ans
