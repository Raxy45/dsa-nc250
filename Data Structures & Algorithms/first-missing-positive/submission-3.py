class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:


        n = len(nums)
        contains1 = False

        # Step 1: Check whether 1 is present and sanitize invalid values
        for i in range(n):
            if nums[i] == 1:
                contains1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if not contains1:
            return 1

        # Step 2: Use index as a hash key, mark presence with negative sign
        for i in range(n):
            val = abs(nums[i])
            idx = val - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Step 3: First positive index is the missing integer
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1