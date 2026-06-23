class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count_arr = {key: 0 for key in nums}
        res = []
        for num in nums:
            count_arr[num] += 1
        
        def solve(count_arr, subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in count_arr:
                if count_arr[i]:
                    subset.append(i)
                    count_arr[i] -= 1

                    solve(count_arr, subset)
                    
                    subset.pop()
                    count_arr[i] += 1
        solve(count_arr, [])
        return res
