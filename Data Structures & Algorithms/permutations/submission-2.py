class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
            