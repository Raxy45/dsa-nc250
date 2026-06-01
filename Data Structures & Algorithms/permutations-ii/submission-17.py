class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            nonlocal ans
            if len(subset)==len(nums):
                ans.append(subset.copy())
                return ans
            
            i = 0
            for i in range(len(nums)):
            # while i<len(nums):
                if nums[i]==float('inf') or (i>0 and nums[i]==nums[i-1]): 
                    # i += 1
                    continue
                subset.append(nums[i])
                temp = nums[i]
                nums[i] = float('inf')

                dfs()

                subset.pop()
                nums[i] = temp
                # i += 1
        ans, subset = [], []
        nums.sort()
        dfs()
        return ans
        