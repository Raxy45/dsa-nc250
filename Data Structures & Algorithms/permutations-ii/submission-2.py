class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        # print(perm, nums, pick)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and pick[i-1]:
                continue
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False