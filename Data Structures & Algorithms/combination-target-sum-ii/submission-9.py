class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        ans = []
        subset = []

        def dfs(start, remain):
            if remain == 0:
                ans.append(subset.copy())
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                if nums[i] > remain:
                    break

                subset.append(nums[i])
                dfs(i + 1, remain - nums[i])
                subset.pop()

        dfs(0, target)
        return ans

    def combinationSum2Rec(self, nums: List[int], target: int) -> List[List[int]]:
        # TC: n log n + 2^(t/min(nums))

        # SC is 2^(t/min(nums))
        ans = []
        subset = []
        nums.sort()
        def dfs(req, idx):
            nonlocal ans
            if req==0:
                ans.append(subset.copy())
                return
            
            if idx==len(nums) or req<0: return

            subset.append(nums[idx])
            dfs(req-nums[idx], idx+1)
            subset.pop()

            while idx<len(nums)-1 and nums[idx] == nums[idx+1]:
                idx += 1
            dfs(req, idx+1)
        dfs(target, 0)
        return ans