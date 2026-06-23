class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,  len(nums)-1

        ans = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>=nums[r]:
                l = mid+1
            else:
                r =mid
        division_point = mid
        if division_point>0:
            l, r = 0, division_point-1
            ans = -1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    r = mid-1
                else:
                    l=mid+1

        l = division_point
        r = len(nums)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l=mid+1
        return -1