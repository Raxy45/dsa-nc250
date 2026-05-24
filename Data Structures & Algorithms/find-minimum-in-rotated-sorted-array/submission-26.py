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
                # The range l to r is already sorted, therefore return l directly
                return nums[l]
            
            m = (l+r)//2
            if nums[l] <= nums[m]:
                # LHS half is already sorted, move to the RHS Half
                l =  m + 1
            else:
                r=m
        return nums[l]
        