class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,  len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            if nums[l]<=nums[mid]:
                # We are in left sorted portion
                if nums[l]<=target and target<=nums[mid]:
                    # target lies in left sorted position
                    r = mid-1
                else:
                    # target lies to the right unsorted position
                    l=mid+1
            else:
                # We are in right sorted portion
                if nums[mid]<=target and target<=nums[r]:
                    # search in right sorted part
                    l = mid+1
                else:
                    r=mid-1
        return False
        