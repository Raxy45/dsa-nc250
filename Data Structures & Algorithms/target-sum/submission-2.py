class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        def solve(i, s):
            nonlocal ans
            if i==n:
                if s==target:
                    ans += 1
                return
            
            solve(i+1, s+nums[i])
            solve(i+1, s-nums[i])
        
        solve(0, 0)
        return ans


            

