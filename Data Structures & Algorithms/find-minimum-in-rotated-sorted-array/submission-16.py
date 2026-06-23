class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-2
        while l<=h:
            mid = (l+h)//2
            print(l, mid, h)
            if nums[l]<=nums[h]:
                return nums[l]
            
            if nums[h]<=nums[mid]:
                l = mid + 1
            else:
                h = mid
            