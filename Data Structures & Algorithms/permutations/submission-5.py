class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(visited):
            print('current', subset)
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in visited: continue
                visited.add(nums[i])
                subset.append(nums[i])

                solve(visited)
                
                visited.remove(nums[i])
                subset.pop()
        ans, subset = [], []
        solve(set())
        return ans