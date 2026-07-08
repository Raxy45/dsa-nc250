class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for i in range(len(nums)-1, -1, -1):
            # curr = max(n1, nums[idx] + n1)
            # print(i, n1, n2, max(nums[i]+n1, n2))
            n1, n2 = n2, max(nums[i]+n1, n2)
        return n2
    def robTopDown(self, nums: List[int]) -> int:
        cache = {}
        def dfs(idx):
            if idx in cache: return cache[idx]
            if idx >=len(nums): return 0
            take = nums[idx] + dfs(idx+2)
            skip = dfs(idx + 1)
            cache[idx] = max(take, skip)
            return cache[idx]
        return dfs(0)

        # At any given point, you will have two options 
            # take the loot
            # skip the loot
        # then return max at each index from the bottom in 
            # recursive solution, store max at the index in cache
