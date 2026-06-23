class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        def solve(idx):
            print('solving for idx', idx)
            if idx == len(nums)-1:
                print('hereeee')
                return 1
            
            if idx in dp:
                return dp[idx]
            
            res = 0
            for i in range(idx, len(nums)):
                if nums[i] > nums[idx]:
                    curr_subs_length = solve(i)
                    print('curr sub length', curr_subs_length, 'parent', idx)
                    print(dp[i])
                    dp[i] = max(dp[i], curr_subs_length)
                    res = max(dp[i], res)
            dp[idx] = max(dp[idx], 1+res)
            return dp[idx]
        for i in range(len(nums)):
            solve(i)
        print(dp.values())
        return max(dp.values())