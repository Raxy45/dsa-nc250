class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[l]<=nums[h]:
                return nums[l]
            
            if nums[h]<nums[m]:
                l = m+1
            else:
                h = m