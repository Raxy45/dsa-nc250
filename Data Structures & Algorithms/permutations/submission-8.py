class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            nonlocal ans
            if len(subset)==len(nums):
                ans.append(subset.copy())
                return ans
            
            for i in range(len(nums)):
                if nums[i]==float('inf'): continue
                subset.append(nums[i])
                temp = nums[i]
                nums[i] = float('inf')

                dfs()

                subset.pop()
                nums[i] = temp
        ans, subset = [], []
        dfs()
        return ans

        