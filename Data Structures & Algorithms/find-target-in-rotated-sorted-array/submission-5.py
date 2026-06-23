class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,  len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            
            if nums[l]<target<nums[m]:
                r=m-1
            else:
                l=m+1
        return -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            
            if nums[l]<=nums[mid]:
                if nums[l]<=target and target<=nums[mid]:
                    r = mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<=target and target<=nums[r]:
                    l = mid+1
                else:
                    r=mid-1
        return -1