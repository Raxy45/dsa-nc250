class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target: return mid

            if nums[l] <= nums[mid]:
                # We are in left sorted position

                if nums[l] <= target < nums[mid]:
                    # answer lies in left sorted part
                    r = mid - 1
                else:
                    # ans lies in right unsorted | sorted part
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    # ans lies in right sorted part
                    l = mid + 1
                else:
                    # ans lies in left unsorted part
                    r = mid - 1
        return -1