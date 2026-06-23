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
        final_mid = mid
        if final_mid<=0:
            return 0
        elif final_mid==len(nums):
            return final_mid

        if nums[mid-1] < target < nums[mid]:
            final_mid= mid-1
        else:
            final_mid = mid+1
        if final_mid<0:
            final_mid = 0
        return final_mid
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