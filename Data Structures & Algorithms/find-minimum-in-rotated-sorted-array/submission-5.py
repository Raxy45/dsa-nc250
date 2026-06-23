class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]>=nums[r]:
                l=m+1
            else:
                r=m
        return nums[m]
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[mid]