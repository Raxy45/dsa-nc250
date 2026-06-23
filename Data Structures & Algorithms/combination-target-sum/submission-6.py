class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset, ans = [], []
        def solve(subset, i, total):
            if total == target:
                ans.append(subset.copy())
                return

            if total > target: return

            for k in range(i, len(nums)):
                subset.append(nums[k])
                total += nums[k]

                solve(subset, k, total)

                subset.pop()
                total -= nums[k]
        solve([], 0, 0)
        return ans