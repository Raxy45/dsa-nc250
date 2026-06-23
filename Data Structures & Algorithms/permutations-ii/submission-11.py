class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
        nums.sort()
        idx = -1
        used = [False] * len(nums)
        def solve(used, subset):
            nonlocal idx
            if len(subset) == len(nums):
                ans.append(subset.copy())
                idx += 1
                return


            for i in range(0, len(nums)):
                # if i<len(nums)-1 and nums[i] == nums[i+1]:
                #     continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue
                if not used[i]:
                    subset.append(nums[i])
                    used[i] = True

                    solve(used, subset)

                    used[i] = False
                    subset.pop()
                
        solve(used, [])
        return ans