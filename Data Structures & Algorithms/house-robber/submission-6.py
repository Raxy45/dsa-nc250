class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {len(nums): 0}
        def dfs(idx, loot):
            if idx in cache: return cache[idx]

            with_loot = 0
            if loot:
                with_loot = nums[idx] + dfs(idx + 1, False)
            without_loot = dfs(idx + 1, True)
            cache[idx] = max(with_loot, without_loot)
            return cache[idx]
        return dfs(0, True)

        # At any given point, you will have two options 
            # take the loot
            # skip the loot
        # then return max at each index from the bottom in 
            # recursive solution, store max at the index in cache
