class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stamina = -1
        # At any index, if there are multiple ways to reach it, only the one with the maximum
        # remaining stamina matters. Any path with less remaining stamina is dominated by the
        # one with more stamina because it can reach every future index that the weaker path
        # can, and possibly more. Therefore, we only need to keep the maximum remaining stamina
        # and can safely discard all other possibilities.
        for i in range(len(nums)-1):
            stamina = max(nums[i], stamina)
            if stamina==0:
                return False
            stamina -= 1

        # at given idx, i just want to store the maximum stamina i can get it will be the one
        # which i am carrying along with or it can be current one
        return True

class SolutionNC:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0