class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0:
                ans = i

            if i == ans:
                count += 1
            else:
                count -= 1
        return ans