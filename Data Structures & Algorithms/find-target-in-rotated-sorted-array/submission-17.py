class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        ans = -1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                # left sorted position
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
            # if nums[l]<= target <nums[m]:
            #     print('in first part', nums[m], l, h)
            #     h = m
            # else:
            #     l = m + 1
        return -1