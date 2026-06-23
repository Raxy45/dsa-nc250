class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def solve(nums):
            if len(nums) == 0:
                return [[]]
            
            perm = solve(nums[1:])
            res = []
            for curr_subset in perm:
                # print('inserting in', curr_subset)
                for i in range(len(curr_subset)+1):
                    temp = curr_subset.copy()
                    temp.insert(i, nums[0])
                    res.append(temp)
            return res
        
        return solve(nums)
        # return res
