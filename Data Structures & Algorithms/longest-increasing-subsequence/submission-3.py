class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        def solve(idx):
            print('solving for idx', idx)
            
            if idx in dp:
                return dp[idx]
            
            res = 1
            for i in range(idx, len(nums)):
                if nums[i] > nums[idx]:
                    curr_subs_length = 1+solve(i)
                    # print('curr sub length', curr_subs_length, 'parent', idx)
                    # print(dp[i])
                    # dp[i] = max(dp[i], curr_subs_length)
                    res = max(curr_subs_length, res)
            dp[idx] = max(dp[idx], res)
            return dp[idx]
        for i in range(len(nums)):
            solve(i)
        print(dp.values())
        return max(dp.values()) if len(dp)>0 else 1