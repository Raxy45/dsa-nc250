class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if (arr_sum%2) > 0: 
            return False
        req_sum = arr_sum/2
        cache = {}
        def dfs(idx, curr):
            # print('need', curr, 'from idx', idx)
            if curr == 0: return True
            if curr <0 or idx==len(nums): return False
            if (curr, idx) in cache: return cache[(curr, idx)]

            cache[(curr, idx)] = dfs(idx+1, curr-nums[idx]) or dfs(idx+1, curr)
            return cache[(curr, idx)]
        return dfs(0, req_sum)

        