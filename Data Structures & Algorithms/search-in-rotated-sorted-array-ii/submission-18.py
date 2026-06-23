class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r= 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            
            while nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1

            if nums[l] <= nums[m]:
                # LHS is sorted
                if target<nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m]<=nums[r] and nums[m]<target<=nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False

        