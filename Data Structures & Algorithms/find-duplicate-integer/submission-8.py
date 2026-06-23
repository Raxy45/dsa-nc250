class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # slow and fast met at some point
                break
        
        slow2, slow = 0, slow
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow