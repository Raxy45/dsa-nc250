class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        ans = -1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            
            if nums[l]<= target <nums[m]:
                h = m
            else:
                l = m + 1
        return -1