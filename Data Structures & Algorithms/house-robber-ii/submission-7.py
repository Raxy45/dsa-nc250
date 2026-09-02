class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max_loot(start, end) -> int:
            n1, n2 = 0, 0
            temp = 0
            for i in range(start, end+1):
                curr = max(nums[i] + n2, n1)
                n2, n1 = n1, curr
            return n1

        n = len(nums)-1
        if len(nums) == 1: return nums[0]
        return max(get_max_loot(0, n-1), get_max_loot(1, n))
