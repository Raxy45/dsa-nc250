class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        return nums[slow]