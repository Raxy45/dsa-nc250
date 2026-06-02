class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, subsets = [], []

        def dfs():
            if len(subsets) == len(nums):
                ans.append(subsets.copy())
                return
            
            for i in range(len(nums)):
                if nums[i]==float('inf') or i>0 and nums[i]==nums[i-1]:
                    continue
                
                subsets.append(nums[i])
                temp = nums[i]
                nums[i] = float('inf')
                dfs()

                subsets.pop()
                nums[i] =temp
        nums.sort()
        dfs()
        return ans