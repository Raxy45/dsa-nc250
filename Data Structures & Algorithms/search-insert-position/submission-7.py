class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        mid = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r=mid-1
        
        print('mid ', mid)
        print('post ',mid)
        if nums[mid-1] < target < nums[mid]:
            return mid-1
        else:
            return mid+1
        if nums[mid]<target:
            mid = mid+1
            return mid
            if mid==len(nums):
                mid = mid-1
            return mid
        

        mid = mid-1
        if mid==-1:
            mid = mid+1

        return mid