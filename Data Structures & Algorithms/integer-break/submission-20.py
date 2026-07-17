class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {0:1}
        # cache[j] = m
        # This represents the maximum product you can get to get j

        i = 0
        def dfs(req_sum):
            # nonlocal i
            # print(cache)
            # print(req_sum)
            if req_sum in cache: return cache[req_sum]
            if req_sum < 0: return 0
            # if i>10: return 0

            curr_mx = float('-inf')
            for i in range(1, n):
                curr_mx = max(i * dfs(req_sum - i), curr_mx)
            cache[req_sum] = curr_mx
            return cache[req_sum]
        return dfs(n)

        