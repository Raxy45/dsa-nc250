class Solution:
    def findDuplicateArr(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            abs_val = abs(nums[i])
            idx = abs_val - 1
            if nums[idx]<0:
                return abs(nums[i])
            nums[idx] = -nums[idx]
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow