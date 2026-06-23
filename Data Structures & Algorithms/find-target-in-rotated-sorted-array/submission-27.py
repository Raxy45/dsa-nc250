class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                # Left part is sorted
                if nums[l]<=target<nums[m]:
                    # ans present in left sorted part
                    h = m - 1
                else:
                    # ans present in right unsorted part
                    l = m + 1
            else:
                # Since left is unsorted, right half is definitely sorted
                if nums[m]<target<=nums[h]:
                    # ans present in right sorted part
                    l = m + 1
                else:
                    # ans is present on left unsorted part
                    h = m - 1
        return -1
