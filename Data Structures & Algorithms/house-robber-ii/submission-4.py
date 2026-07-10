class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max_loot(start, end):
            n1, n2 = 0, 0
            for i in range(start, end, -1):
                n1, n2 = max(nums[i]+n2, n1), n1
            return n1

        n = len(nums)-1
        if len(nums) == 1: return 0
        return max(get_max_loot(n, 0), get_max_loot(n-1, -1))
