class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for n in nums:
            my_map[n] = my_map.get(n, 0) + 1

        for n in my_map:
            if my_map[n] > 1:
                return True
        return False
        