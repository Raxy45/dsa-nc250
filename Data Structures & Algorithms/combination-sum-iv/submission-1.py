class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        dp = {}
        def solve(target):
            nonlocal ans
            if target == 0:
                ans += 1
                return
            
            
            for n in nums:
                if n<=target:
                    solve(target-n)
        solve(target)
        return ans