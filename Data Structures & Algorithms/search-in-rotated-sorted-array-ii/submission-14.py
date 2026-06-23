from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # identify the sorted part by comparing nums[l] and nums[m]
        # check if the ans present in sorted -> yes -> search in this sorted part, no -> search in unsorted part
        l, r = 0,  len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            
            while nums[l] == nums[l+1]:
                l += 1
            
            while nums[r] == nums[r-1]:
                r -= 1
            if nums[l]<=nums[mid]:
                # We are in left sorted portion
                if nums[l]<=target and target<=nums[mid]:
                    # target lies in left sorted position
                    r = mid-1
                else:
                    # target lies to the right unsorted position, discard left sorted part
                    l=mid+1
            else:
                # Since left is unsorted, definitely right is sorted. We are in right sorted portion
                if nums[mid]<=target and target<=nums[r]:
                    # search in right sorted part
                    l = mid+1
                else:
                    # ans lies in left unsorted part, discard right sorted part
                    r=mid-1
        return False