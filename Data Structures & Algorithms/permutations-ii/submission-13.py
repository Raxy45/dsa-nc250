class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def solve(visited):
            print('solved called for', visited)
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return
            
            i=0
            while i<(len(nums)):
                print(i, visited[i], subset)
                if not visited[i]:
                    subset.append(nums[i])
                    visited[i] = True

                    solve(visited)

                    subset.pop()
                    visited[i] = False
                    while (i<len(nums)-1 and nums[i] == nums[i+1]):
                        i += 1
                i += 1
        
        nums.sort()
        ans, subset, visited = [], [], [False] * len(nums)
        solve(visited)
        return ans