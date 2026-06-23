class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
        used = [False] * len(nums)
        def solve(used, subset):
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return

            for i in range(0, len(nums)):
                if used[i]:
                    continue
                
                subset.append(nums[i])
                used[i] = True

                solve(used, subset)

                subset.pop()
                used[i] = False
        solve(used, [])
        return ans