class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < (len(nums)-1):
            next_max_reach = 0
            for i in range(l, r+1):
                next_max_reach = max(next_max_reach, i + nums[i])
            
            l = r+1
            r = next_max_reach
            res += 1
        return res

        