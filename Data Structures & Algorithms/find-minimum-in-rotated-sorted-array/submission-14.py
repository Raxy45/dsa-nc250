class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[l] <= nums[r]:
                # entire array is sorted
                res = min(res, nums[l])
                break
            
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m 
        return res