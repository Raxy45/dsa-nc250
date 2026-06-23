class Solution:
    def permute(self, nums):
        res = []
        def solve(nums, idx):
            if idx == len(nums):
                res.append(nums.copy())
                return
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                
                solve(nums, idx+1)

                nums[idx], nums[i] = nums[i], nums[idx]
        solve(nums, 0)
        return res
        
    def permute2(self, nums: List[int]) -> List[List[int]]:
        bool_arr = [False] * len(nums)
        ans = []

        def solve(bool_arr, subset):
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return

            for i in range(len(nums)):
                if not bool_arr[i]:
                    subset.append(nums[i])
                    bool_arr[i] = True

                    solve(bool_arr, subset)

                    subset.pop()
                    bool_arr[i] = False
        solve(bool_arr, [])
        return ans
            