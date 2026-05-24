class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. One half is always sorted.
        # 2. Determine which half is sorted.
        # 3. Check whether target lies inside that sorted range.
        # 4. Discard the impossible half.
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                # LHS is sorted
                if target < nums[l] or target>nums[m]:
                    # target is lower than l  (can be in RHS)
                    # target is larger than m (can be in RHS)
                    l = m + 1
                else:
                    r = m - 1
            else:
                # Right can be sorted or unsorted
                if nums[r] > nums[m] and nums[m]<target<=nums[r]:
                    # RHS is perfectly sorted and also the answer lies in 
                    # range of nums[m] to nums[r]
                    l = m + 1
                else:
                    r = m - 1

        return -1