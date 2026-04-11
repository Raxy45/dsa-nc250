class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        dp = defaultdict(int)
        def solve(l, r):
            if l>r: return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = max(nums[l]-solve(l+1, r), nums[r]-solve(l, r-1))
            return dp[(l, r)]
        # print(solve(0, len(nums)-1))
        
        return True if solve(0, len(nums)-1) > 0 else False