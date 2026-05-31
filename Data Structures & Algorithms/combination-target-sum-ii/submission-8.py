class Solution:
    def combinationSum2Loop(self, nums, t):
        ans, subset = [], []
        def dfs(req, idx):
            nonlocal ans
            if req==0:
                ans.append(subset.copy())
                return
            
            if req<0 or idx>=len(nums): return
            print('current', idx, len(nums))
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                dfs(req-nums[i], i+1)

                subset.pop()
                dfs(req, i+1)
            
        dfs(t, 0)
        return ans

    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
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