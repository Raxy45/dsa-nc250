class Solution:
    def findMinME(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] >= nums[r]:
                # ans lies to the RHS
                l = m + 1
            else:
                r = m
        # print(l, m, r)
        return nums[m]
    
    def findMin(self, nums):
        l , r = 0, len(nums)-1
        while l<=r:
            if nums[l]<=nums[r]:
                return nums[l]
            
            m = (l+r)//2
            if nums[l] <= nums[m]:
                l =  m + 1
            else:
                r=m
        return nums[l]
        