class Solution:
    # When nums[l] == nums[m] == nums[r],
    # duplicates hide the pivot and we cannot
    # determine which half is sorted.
    #
    # Since nums[m] != target (already checked),
    # discarding nums[l] and nums[r] is safe.
    #
    # Shrink both ends until the ambiguity is removed,
    # then continue normal rotated-array binary search.

    # ex [1,0, 1,1,1,1]
    # then in such cases, the l==m and if we did not have dupe skipping logic.
    # We would assume LHS half is sorted, but it is not the case. Therefore
    # we are skipping when l==m, the same goes with r==m

    # It is safe to skip them? Yes, cause we already check if nums[m]==target:
    # since it is not target, we can easily shrink when l==m==r

    # TC also goes from logn to n. Why?
    # example arr like [1,1,1,1,1,1,11,1,1,1,1,1]
    # then you can't do Binary search -> n, n/2, n/4, n/8
    # you are forced to reduce 2 elements at a time. Therefore, TC is increased.
    def search(self, nums: List[int], target: int) -> bool:
        l, r= 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            
            while l<=r and nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1

            if l>r:
                break
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

        