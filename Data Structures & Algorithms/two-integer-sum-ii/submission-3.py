class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l<=r:
            rs = nums[l] + nums[r]
            if rs==target:
                return [l+1, r+1]
            
            if rs < target:
                l += 1
            else:
                r -= 1
        return []