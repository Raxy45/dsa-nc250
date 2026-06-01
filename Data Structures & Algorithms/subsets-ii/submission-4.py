class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, subset = [], []
        def dfs(i):
            nonlocal ans
            if i==len(nums):
                ans.append(subset.copy())
                return
                    
            # for i in range(idx, len(nums)):
            #     if i>idx and nums[i] == nums[i-1]: continue

            #     subset.append(nums[i])
            #     dfs(i+1)
            #     subset.pop()
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            while i<len(nums)-1 and nums[i] == nums[i+1]: 
                # skipping
                i+= 1
            dfs(i+1)
        dfs(0)
        return ans