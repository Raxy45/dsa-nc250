class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[l]<=nums[r]:
                res = min(res, nums[l])
                break
            
            res = min(res, nums[mid])
            if nums[l]<=nums[mid]:
                l = mid + 1
            else:
                r = mid-1
        return res