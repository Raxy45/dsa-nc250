class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {(len(nums), True): 0, (len(nums), False): 0}
        def dfs(idx, loot):
            if (idx, loot) in cache: return cache[(idx, loot)]

            with_loot = 0
            if loot:
                with_loot = nums[idx] + dfs(idx + 1, False)
            without_loot = dfs(idx + 1, True)
            cache[(idx, loot)] = max(with_loot, without_loot)
            return cache[(idx, loot)]
        print(cache)
        return dfs(0, True)

        # At any given point, you will have two options 
            # take the loot
            # skip the loot
        # then return max at each index from the bottom in 
            # recursive solution, store max at the index in cache
