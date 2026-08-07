class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stamina = -1
        for i in range(len(nums)-1):
            stamina = max(nums[i], stamina)
            if stamina==0:
                return False
            stamina -= 1

        return True