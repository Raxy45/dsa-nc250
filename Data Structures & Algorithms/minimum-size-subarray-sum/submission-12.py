class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)+1
        i = 0
        c_s = 0
        for j in range(len(nums)):
            c_s += nums[j]
            while c_s >= target:
                ans = min(ans, j-i+1)
                c_s -= nums[i]
                i += 1
        return ans if ans!=len(nums)+1 else 0