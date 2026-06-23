class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        def solve(l, r):
            if l>r: return 0

            # print('curr', l, r)
            if nums[l]>=nums[r]:
                # print('using l', nums[l])
                curr = nums[l] - solve(l+1, r)
            else:
                # print('using r', nums[r])
                curr = nums[r] - solve(l, r-1)
            # print('curr', curr)
            return curr
        # print(solve(0, len(nums)-1))
        
        return True if solve(0, len(nums)-1) > 0 else False