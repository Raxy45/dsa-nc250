class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                # Left part is sorted
                if nums[l]<=target<nums[mid]:
                    h = m - 1
                else:
                    r = m + 1
            else:
                if nums[m]<target<=nums[r]:
                    l = m + 1
                else:
                    h = m - 1
        return -1
